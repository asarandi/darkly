# http://192.168.99.100/?page=feedback

```
<script type="text/javascript">
function validate_required(field,alerttxt)
{
with (field) {
  if (value==null||value=="") {
    alert(alerttxt);return false;
  }
  else {
    return true;
  }
 }
}
function validate_form(thisform) {
with (thisform) {
  if (validate_required(txtName,"Name can not be empty.")==false)
  {txtName.focus();return false;}
  
  if (validate_required(mtxMessage,"Message can not be empty.")==false)
  {mtxMessage.focus();return false;}
  
  }
}
</script>
<center><h2> Feedback </h2></center>
<form method="post" name="guestform" onsubmit="return validate_form(this)">
	<table width=50% border="0" cellpadding="2" cellspacing="1">
		<tr style="background-color:transparent;border:none;">
			<td width="110">Name *</td>
			<td> <input name="txtName" type="text" size="30" maxlength="10"> </td>
		</tr>
		<tr style="background-color:transparent;border:none;">
			<td width="110">Message *</td>
			<td> <textarea name="mtxtMessage" cols="50" rows="3" maxlength="50"></textarea> </td>
		</tr>
		<tr style="background-color:transparent;border:none;">
			<td width="110">&nbsp;</td>
			<td><input name="btnSign" type="Submit" value="Sign Guestbook" onClick="return checkForm();"></td>
		</tr>
	</table>
</form> 
```

the page seems to be poorly written,
the form has an input of **type** *Submit* which has an `onClick` attribute `return checkForm();`
however there is no such javascript function on this page,
when pressing the button it generates an error in chrome developer tools,
in "Console" section of the developer tools we can see

```
?page=feedback:83 Uncaught ReferenceError: checkForm is not defined
    at HTMLInputElement.onclick (?page=feedback:83)
onclick @ ?page=feedback:83
```

the form element has a `onsubmit` attribute which calls `validate_form()`, which also seems broken because in the form the textarea has **name** *mtxtMessage* but in javascript validation function it is *mtxMessage*, so one character element name misspelling crippled the javascript validation

as a result, the length of the message is never validated


but even if the javascript was functional and properly checked the lengths of both fields *name* and *message*, it would still be possible to perform an http post request with empty variables .. (for example via curl, or python's requests)

while playing with the page, i discovered that it will only show the flag when the *mtxtMessage* is set to certain values (i was testing with one character string *a*)

the page shows
```
THE FLAG IS : 0FBB54BBF7D099713CA4BE297E1BC7DA0173D8B3C21C1811B916A3A86652724E
```

i further tried other characters like *b* which did not work, and *c* which did work,
so i wrote a small script to test all possible values from 0 to 255

```
#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup

base='http://192.168.99.100/?page=feedback'

for i in range(256):
    req = requests.post(base, data = {
	    'txtName':'',
	    'mtxtMessage': chr(i),
	    'btnSign': 'Sign Guestbook'
	    })
    soup = BeautifulSoup(req.text, 'html.parser')
    subj = soup.find('form').find_next_sibling()
    if subj.name != 'table':
        print("%03d %02x %c" % (i, i, chr(i)))
```


here are the results:
```
dec hex
065 41 A
067 43 C
069 45 E
073 49 I
076 4c L
080 50 P
082 52 R
083 53 S
084 54 T
097 61 a
099 63 c
101 65 e
105 69 i
108 6c l
112 70 p
114 72 r
115 73 s
116 74 t
```

so the character set is `aceilprst` both uppercase and lowercase
which appears to be an anagram of the word `particles`
makes me think that the php code is something like this:
```
if (isset($_POST['mtxtMessage'])) {
	$m = $_POST['mtxtMessage'];
	if ((strlen($m) == 1) && ((strpos("particles", strtolower($m)) !== false) {
		show_flag();
		}
}
```

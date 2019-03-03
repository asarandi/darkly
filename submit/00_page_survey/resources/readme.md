# http://192.168.99.100/?page=survey

here we notice that each row of the "***Make your choice***" table is an html *form* element,
the form *action* is set to `#` which is self, and the form method is set to `post`

form has several inputs:

 **input** `name` *sujet*, `type` *hidden*, value range from `2` to `6`
   
 **input** `name` *valeur*, `type` *select*, value range from `1` to `10`

<br />

the "valeur" element has a `onchange` javascript attribute, which submits the form

if we submit a post request with the `valeur` greater than 10, the page shows the flag:


**`The flag is 03a944b434d5baff05f46c4bede5792551a2595574bcafc9a6e25f67c382ccaa`**

<br />

**moral of the story:**
when variables are passed in the url (html get request) it is very simple to change them directly in the browser,
with a post request its slightly more complex but can still lead to undesired behavior, so user data must be sanitized/validated

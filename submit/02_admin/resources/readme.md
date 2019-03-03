# http://192.168.99.100/admin/

the admin page requires a username and a password,

if we look at */robots.txt* we notice a folder called */whatever*
inside the */whatever* folder we find the _**htpasswd**_ file

inside the file we find
```
root:8621ffdbc5698829397d97767ac13db3
```

a quick google of the hash reveals that its an MD5 hash of the string **_dragon_**


once we try the combination `root:dragon` for the */admin* page
we get our next flag
```
d19b4823e0d5600ceed56d5e896ef328d7a2b9e7ac7e80f4fcdb9b10bcb3e7ff
```
and a nice gif, lol

[![whoami.gif](whoami.gif "whoami.gif")](whoami.gif "whoami.gif")

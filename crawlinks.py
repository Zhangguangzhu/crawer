# -*- coding: utf-8 -*-

import urllib.request
import re
url = 'https://www.csdn.net'
header = ('User-Agent',"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36")
opener = urllib.request.build_opener()
opener.addheaders = [header]
urllib.request.install_opener(opener)
htmldoc = str(urllib.request.urlopen(url).read())
pattern = '(https?://\S+(?<!jpg))\"'
res = re.findall(pattern, htmldoc)
with open('linktest1.txt', 'w') as f:
	for link in res:
		f.write(link+'\n')

pattern = '(https?://\S+)\"'
res = re.findall(pattern, htmldoc)
with open('linktest2.txt', 'w') as f:
	for link in res:
		f.write(link+'\n')


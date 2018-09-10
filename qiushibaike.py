# -*- coding: utf-8 -*-

import urllib.request, re,sys
url = 'https://www.qiushibaike.com'
header = ("User-Agent", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36")
opener = urllib.request.build_opener()
opener.addheaders = [header]
urllib.request.install_opener(opener)
pattern = '<div class=\"author clearfix\">.*?<h2>\n(\S+)\n</h2>.*?<div class=\"(?:content|thumb)\">.*?<span>(.*?)</span>'
# pattern = '<div class=\"author clearfix\">.*?<h2>\n(\S+)\n</h2>'

htmldoc = urllib.request.urlopen(url).read().decode('utf-8')
res = re.findall(pattern, htmldoc, re.S)
for author_content in res:
	print("author:%s\ncontent:%s" % (author_content[0], author_content[1].replace("<br/>", "\n")))

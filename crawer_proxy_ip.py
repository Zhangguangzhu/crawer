# -*- coding: utf-8 -*-

import urllib.request, urllib.error

import re
from sqlalchemy import Column, String, create_engine, Integer, Float
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('mysql+mysqldb://root:iie123!@#@localhost:3306/python_sql?charset=utf8')
Base = declarative_base()
class ProxyIp(Base):

	__tablename__ = 'proxyip'
	id = Column(Integer, primary_key=True)
	ip = Column(String(20))
	type = Column(String(6))
	addr = Column(String(30))
	port = Column(String(6))
	ping = Column(Float)
	isok = Column(Integer,default=0)

Base.metadata.create_all(engine)
DBsession = sessionmaker(bind=engine)
session = DBsession()

url = 'http://www.xicidaili.com/nn/1'

def addip(ip, port, addr, type, ping):
	session.add(ProxyIp(ip=ip,port=port,addr=addr,type=type,ping=ping))


def crawer(url):
		req = urllib.request.Request(url)
		req.add_header("User-Agent","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36")
		htmlDoc = urllib.request.urlopen(req).read().decode('utf-8')
		proxyIpInfoPattern = r'<tr class=\"odd\">.*?</td>\s+<td>(.*?)</td>\s+<td>(.*?)</td>\s+<td>(.*?)</td>\s+<td class=\"country\".*?</td>\s+<td>(.*?)</td>.*?<div title=\"(.*?)秒\"'
		res = re.findall(proxyIpInfoPattern,htmlDoc,re.S)
		for info in res:
			if float(info[4]) < 1.0:
				addrPattern = r'<a.*?>(\S+)</a>'
				addr = re.findall(addrPattern, info[2])
				addip(info[0], info[1], addr, info[3], info[4])
		session.commit()

def connectTest():
	ipList = session.query(ProxyIp).all()
	for ipinfo in ipList:
		proxy = urllib.request.ProxyHandler({ipinfo.type:ipinfo.ip})
		opener = urllib.request.build_opener(proxy)
		urllib.request.install_opener(opener)
		try:
			urllib.request.urlopen('http://www.baidu.com', timeout=3)
			print('ip:%s is available' % ipinfo.ip)
			ipinfo.isok = 1
		except urllib.error.URLError as e:
			if hasattr(e,"code"):
				print(e.code)
			elif hasattr(e,"reason"):
				print(e.reason)
			ipinfo.isok = 0
		except Exception as e:
			print(ipinfo.ip, e)
			ipinfo.isok = 0
	session.commit()

def useproxy(url):
	connectTest()
	ipList = session.query(ProxyIp.ip).filter(ProxyIp.isok == 1).all()
	proxy = urllib.request.ProxyHandler({ipinfo.type: ipinfo.ip})
	opener = urllib.request.build_opener(proxy)
	urllib.request.install_opener(opener)
	try:
		urllib.request.urlopen(url, timeout=3)
	except urllib.error.HTTPError as e:
		print(e.code, e.reason)

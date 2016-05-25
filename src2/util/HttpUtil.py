#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 
# Author: felix_mao
# Date:2016年5月25日
#

import urllib  
import urllib2,cookielib
import StringIO
import zlib
import gzip

hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'gzip, deflate, sdch',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}


class HttpUtil:
	'封装了通过HTTP获取网页的类'
	
	#获取网页html内容
	@staticmethod 
	def getPage(url):		
		user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6' ;
		values = {'name' : 'Michael Foord', 
          'location' : 'pythontab' } 
		headers = { 'User-Agent' : user_agent }
		data = urllib.urlencode(values) 
		request = urllib2.Request(url, "", headers); 
		try:
			response = urllib2.urlopen(request);
			return response.read()
		except:
			return HttpUtil.getPage2(url)
		
		
	#获取网页html内容,
	@staticmethod 
	def getPage2(url):				
		req = urllib2.Request(url, headers=hdr)
		try:
			page = urllib2.urlopen(req)
		except urllib2.HTTPError, e:
			print e.fp.read()
		content = page.read()
		try:
			content = gzip.GzipFile('', 'rb', 9, StringIO.StringIO(content))
			content = content.read()
		except:
			content = StringIO.StringIO(zlib.decompress(content))
			content = content.read()
		return content
		
if __name__=='__main__':
	url = 'http://finance.sina.com.cn/roll/2016-05-25/doc-ifxsqtya6053789.shtml'
	print HttpUtil.getPage(url)
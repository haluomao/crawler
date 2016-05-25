# -*- coding: utf-8 -*-
import re
import urllib  
import urllib2  
from sgmllib import SGMLParser  
import util.FileUtil
import util.HtmlUtil

class ListName(SGMLParser):  
    is_a=""  
    name=[]  
    def start_a(self, attrs):  
        self.is_a=1  
    def end_a(self):  
        self.is_a=""  
    def handle_data(self, text):  
        if self.is_a:  
                self.name.append(text)  
				
				
class Spider:
	
	def __init__(self):
		self.siteURL = 'http://roll.finance.sina.com.cn/finance/zq1/ssgs/index_';
    
	#获取网页html内容
	def getPage(self, url):		
		user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)' ;
		values = {'username' : 'cqc',  'password' : 'XXXX' }  ;
		headers = { 'User-Agent' : user_agent }  ;
		request = urllib2.Request(url, '', headers); 
		response = urllib2.urlopen(request);
		return response.read();
		
		
	def getContents(self, url):
		page = self.getPage(url);
		pattern = re.compile(r'<a href=.*>.*</>', re.S);
		items = re.findall(pattern,page);
		for item in items:
			print item[0],item[1],item[2],item[3],item[4];
		return items;
		
	'''
	<a href="http://finance.sina.com.cn/roll/2016-05-19/doc-ifxskpkx7476996.shtml" target="_blank">美都能源拟取消2015年度利润分配预案用于公司运营</a>
	        #pattern = re.compile('<div class="list-item".*?pic-word.*?<a href="(.*?)".*?<img src="(.*?)".*?<a #class="lady-name.*?>(.*?)</a>.*?<strong>(.*?)</strong>.*?<span>(.*?)</span>', re.S)
			
	url = 'http://www.server.com/login'
	user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'  
	values = {'username' : 'cqc',  'password' : 'XXXX' }  
	headers = { 'User-Agent' : user_agent }  
	data = urllib.urlencode(values)  
	request = urllib2.Request(url, data, headers)  
	response = urllib2.urlopen(request)  
	page = response.read() 
	'''

class URLLister(SGMLParser):  
	self.urls = [];
	def start_a(self, attrs):                       
		href = [v for k, v in attrs if k=='href']   
		if href:  
			self.urls.extend(href)  
			


spider = Spider();
#spider.getContents(1)
url = "http://roll.finance.sina.com.cn/finance/zq1/ssgs/index_1.shtml";
print spider.getContents(url);

lister=URLLister() 
lister.feed(spider.getPage(url));

'''
listname=ListName()  
listname.feed(spider.getPage(url))  
print listname.name  
'''
#!/usr/bin/python
# -*- coding: UTF-8 -*-
from sgmllib import SGMLParser  
from bs4 import BeautifulSoup


class HtmlUtil:
	'封装了获取Html元素操作的类'
	encode='utf-8';
	
	#通过css选择器
	def select(self, content, expr):
		soup = BeautifulSoup(content);
		return soup.select(expr);
		
	#通过css选择器获取内容
	def select_v(self, content, expr):
		soup = BeautifulSoup(content);
		return soup.select(expr)[0].string;
		
	#通过css选择器获取内容
	def select_vs(self, content, expr):
		soup = BeautifulSoup(content);
		res = [];
		for ele in soup.select(expr):
			res.append(ele.string);
		return res;
		
	#通过选择器获取<a>中的链接和内容
	def select_href_text(self, content, expr):
		soup = BeautifulSoup(content);
		res = {};
		for ele in soup.select(expr):
			href = ele.href;
			print href;
			text = ele.string;
			res[text]=href;
		return res;

	#正则表达式或attr
	# text=["Tillie", "Elsie", "Lacie"]	
	def findAll(self, content, expr):
		soup = BeautifulSoup(content);
		return soup.find_all(expr);
		
	#soup.find_all("a", class_="sister")
	def findAll(self, content, expr1, expr2):
		soup = BeautifulSoup(content);
		return soup.find_all(expr1, expr2);
		
	#格式化网页输出
	def printP(self, content):
		soup = BeautifulSoup(content);
		print soup.prettify();	

s = '''
<ul class="list_009">
			
				<li><a href="http://finance.sina.com.cn/roll/2016-05-19/doc-ifxskpkx7476996.shtml" target="_blank">美都能源拟取消2015年度利润分配预案用于公司运营</a><span>(05月19日 18:29)</span></li>
					
					
				<li><a href="http://finance.sina.com.cn/stock/s/2016-05-19/doc-ifxsktkr5763665.shtml" target="_blank">创意信息董事长增持公司股份26,000股</a><span>(05月19日 18:22)</span></li>
					
					
				<li><a href="http://finance.sina.com.cn/stock/s/2016-05-19/doc-ifxsktkp8994749.shtml" target="_blank">5月19日晚间上市公司利好消息一览</a><span>(05月19日 18:11)</span></li>
					
					
				<li><a href="http://finance.sina.com.cn/stock/s/2016-05-19/doc-ifxsktkp8994748.shtml" target="_blank">5月19日上市公司晚间公告速递</a><span>(05月19日 18:11)</span></li>
					
					
				<li><a href="http://finance.sina.com.cn/stock/s/2016-05-19/doc-ifxskpkx7473198.shtml" target="_blank">洋河“不务正业”寻找新业务增长点：进口啤酒</a><span>(05月19日 17:12)</span></li>
					
		</ul>
'''

htmlUtil = HtmlUtil();
expr='div.video-summary-data a[href^=/video]'
print htmlUtil.select_vs(s, 'title');	
#print htmlUtil.select_href_text(s, 'ul li a').items();
for i in htmlUtil.select_href_text(s, 'ul li a'):
	print i;
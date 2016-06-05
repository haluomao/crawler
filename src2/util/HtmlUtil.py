#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 
# Author: felix_mao
# Date:2016年5月25日
#
from sgmllib import SGMLParser  
from bs4 import BeautifulSoup

class HtmlUtil:
	'封装了获取Html元素操作的类'
	encode="utf-8";
	
	#通过css选择器
	@staticmethod 
	def select(content, expr):
		soup = BeautifulSoup(content, from_encoding=HtmlUtil.encode)
		return soup.select(expr)
		
	#通过css选择器获取内容
	@staticmethod 
	def select_v(content, expr):
		soup = BeautifulSoup(content, from_encoding=HtmlUtil.encode)
		return soup.select(expr)[0].string
		
	#通过css选择器获取内容
	@staticmethod 
	def select_vs(content, expr):
		soup = BeautifulSoup(content, from_encoding=HtmlUtil.encode)
		res = [];
		#for ele in soup.select(expr):
		#	res.append(ele.string);
		map(lambda x:res.append(x.string), soup.select(expr))
		return res
	
	@staticmethod 
	def select_all(content, expr):
		soup = BeautifulSoup(content, from_encoding=HtmlUtil.encode)
		res = [];
		for ele in soup.select(expr):
			if None==ele.string:
				res.append(ele)
			else:
				res.append(ele.string)
		return res;	
	
	@staticmethod 
	def select_text(content, expr):
		soup = BeautifulSoup(content, from_encoding=HtmlUtil.encode)
		res = [];
		for ele in soup.select(expr):
			res.append(ele.get_text())
		return res
		
	#通过选择器获取<a>中的链接和内容
	#usage：
	#	for (k,v) in htmlUtil.select_href_text(s, 'ul li a').items():
	#		print k+" "+v;
	@staticmethod 
	def select_href_text(content, expr):
		soup = BeautifulSoup(content, from_encoding=HtmlUtil.encode)
		res = {};
		for ele in soup.select(expr):
			href = ele.get('href');
			text = ele.string;
			res[text]=href;
		return res;

	#正则表达式或attr
	# text=["Tillie", "Elsie", "Lacie"]	
	def findAll1(self, content, expr):
		soup = BeautifulSoup(content, from_encoding=self.encode)
		return soup.find_all(expr);
		
	#soup.find_all("a", class_="sister")
	@staticmethod 
	def findAll(content, expr1, expr2):
		soup = BeautifulSoup(content, from_encoding=self.encode)
		return soup.find_all(expr1, expr2)
		
	#格式化网页输出
	def printP(self, content):
		soup = BeautifulSoup(content)
		print soup.prettify()
		
if __name__ == '__main__':

	content='''
	<p>　　6月2日晚，<span id="stock_3001042"><a class="keytip" href="http://quote.eastmoney.com/SZ300104.html" target="_blank">乐视网</a></span><span id="quote_3001042"></span>(300104.SZ)发布重大资产重组公告，拟以发行股份及支付现金相结合的方式收购乐视影业100%股权，合计作价98亿元收购乐视控股等44名股东持有的乐视影业100%股权，交易对方包括张艺谋、郭敬明、孙红雷等多位明星；同时拟向不超过五名特定对象定增配套募资不超过50亿元，拟用于支付现金对价、补充流动资金及投拍电影和生态自制剧等。乐视网于6月3日复牌。</p>'''
	soup = BeautifulSoup(content)
	print soup.get_text()
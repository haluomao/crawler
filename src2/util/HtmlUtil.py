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
		return soup.select(expr);
		
	#通过css选择器获取内容
	@staticmethod 
	def select_v(content, expr):
		soup = BeautifulSoup(content, from_encoding=HtmlUtil.encode)
		return soup.select(expr)[0].string;
		
	#通过css选择器获取内容
	@staticmethod 
	def select_vs(content, expr):
		soup = BeautifulSoup(content, from_encoding=HtmlUtil.encode)
		res = [];
		for ele in soup.select(expr):
			res.append(ele.string);
		return res;
		
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
	def findAll(self, content, expr):
		soup = BeautifulSoup(content, from_encoding=self.encode)
		return soup.find_all(expr);
		
	#soup.find_all("a", class_="sister")
	def findAll(self, content, expr1, expr2):
		soup = BeautifulSoup(content, from_encoding=self.encode)
		return soup.find_all(expr1, expr2);
		
	#格式化网页输出
	def printP(self, content):
		soup = BeautifulSoup(content);
		print soup.prettify();	
		
if __name__ == '__main__':
	content='adfadf'
	soup = HtmlUtil.select(content, ' ')
	print soup
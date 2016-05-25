#!/usr/bin/python
# -*- coding: UTF-8 -*-
import codecs
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

class FileUtil:
	'用与封装文件读写的类'
	encode='utf-8';
	@staticmethod 
	def put(filePath, content):
		with open(filePath, "w") as file:
			file.write(content);
			
	@staticmethod 
	def append(filePath, content):
		with open(filePath, "a") as file:
			file.write(content);
	
	@staticmethod 
	def appendline(filePath, content):
		with open(filePath, "a") as file:
			file.write(content+"\n");

	# 按行读
	@staticmethod 
	def readlines(filePath):
		with codecs.open(filePath, "r", FileUtil.encode) as file:
			return file.readlines();

	'''
	for i in readlines(filePath):
		print i;
	'''

	@staticmethod 
	def read(filePath):
		with codecs.open(filePath, "r", FileUtil.encode) as file:
			return file.read()
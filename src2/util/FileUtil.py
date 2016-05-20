#!/usr/bin/python
# -*- coding: UTF-8 -*-
import codecs

class FileUtil:
	'用与封装文件读写的类'
	encode='utf-8';
	def put(self, filePath, content):
		with open(filePath, "w") as file:
			file.write(content);

	def append(self, filePath, content):
		with open(filePath, "a") as file:
			file.write(content);

	def appendline(self, filePath, content):
		with open(filePath, "a") as file:
			file.write(content+"\n");

	# 按行读
	def readlines(self, filePath):
		with codecs.open(filePath, "r", self.encode) as file:
			return file.readlines();

	'''
	for i in readlines(filePath):
		print i;
	'''

	def read(self, filePath):
		try:
			file = codecs.open(filePath, "r", self.encode);
			res = file.read();
		finally:
			if file:
				file.close();
			return res;

def testFileUtil():
	filePath='C:\Users\maofagui\Desktop\MailSender.java';
	f=FileUtil();
	print f.read(filePath);
	#f.put(filePath+'0', 'Hello');

#testFileUtil();
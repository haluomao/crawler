#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 
# Author: felix_mao
# Date:2016年5月25日

class StrUtil:
	'处理String的工具类'
	
	#删除前后空格
	@staticmethod 
	def trim(src):
		return src.strip();
		
if __name__ == '__main__':
	src=" hello world      "
	print StrUtil.trim(src)
		
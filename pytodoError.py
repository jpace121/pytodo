#!/usr/bin/env python

class OptionError(Exception):
	def __init__(self,function,option):
		self.function = function
		self.option = option
		

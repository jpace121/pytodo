#!/usr/bin/env python

import argparse
import os
from pytodoError import OptionError

def addf(todofile,option):
	if option:
		with opentodofile(todofile) as todfile:
			with open('.~todofile','w') as tmpfile:
				for line in todfile.readlines():
					tmpfile.write(line)
				tmpfile.write("* " + option + "\n")
		os.rename('.~todofile',todofile)
	else:
		raise OptionError("add",option)

def removef(todofile,option):
	if option:
		with opentodofile(todofile) as todfile:
			with open('.~todfile','w') as tmpfile:
				for line in todfile:
					if option in line:
						line = line.replace('*','-',1)
						tmpfile.write(line)
					else:
						tmpfile.write(line)
		os.rename('.~todfile',todofile)
	else:
		raise OptionError("remove",option)

def listf(todofile,option):
	with opentodofile(todofile) as todfile:
		lines = todfile.readlines()
		if option == "" or option == "todo":
			for line in lines:
				if line[0] == '*':
					print line.rstrip()
		elif option == "all":
			for line in lines:
				print line.rstrip()
		elif option == "done":
			for line in lines:
				if line[0] == "-":
					print line.rstrip()
		else:
			raise OptionError("list",option)

def opentodofile(fileLoc):
	if os.path.exists(fileLoc):
		todofile = open(fileLoc,'r')
	else:
		todofile = open(fileLoc,'w+')

	return todofile

def main():
	#Parse all the input stuffs
	parser = argparse.ArgumentParser(description="Simple ToDo Script.  Find me\
	    on GitHub.")
	parser.add_argument("command", type=str, choices=['add','remove','list',
		'delete'], help="What needs to be accomplished.")
	parser.add_argument("option", type=str, nargs = '?', default = "", 
	    help = "Specify option for specific subcommand.")
	parser.add_argument("-f","--file",type=str,action='store',dest="fileloc",
		default='.todfile')
	args = parser.parse_args()

	#Handle the input file
	todofile = args.fileloc;
	try:
		if args.command == 'add':
			addf(todofile,args.option)
		elif args.command == 'remove':
			removef(todofile,args.option)
		elif args.command == 'list':
			listf(todofile,args.option)
	except OptionError as err:
		print "\"" + err.option + "\" is not a valid option for " + err.function
		parser.print_help()	

if __name__ == '__main__':
	main()

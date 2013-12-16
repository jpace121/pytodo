#!/usr/bin/env python

import argparse
import os

def addf(todfile,option,parser):
	if option:
		with open('.~todfile','w') as tmpfile:
			for line in todfile.readlines():
				tmpfile.write(line)
			tmpfile.write("* " + option + "\n")
		os.rename('.~todfile','.todfile')
	else:
		parser.print_help()

def removef(todfile,option,parser):
	if option:
		with open('.~todfile','w') as tmpfile:
			for line in todfile:
				if option in line:
					line = line.replace('*','-',1)
					tmpfile.write(line)
				else:
					tmpfile.write(line)
		os.rename('.~todfile','.todfile')
	else:
		parser.print_help()

def listf(todfile,option,parser):
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
		parser.print_help()

def main():
	#Parse all the input stuffs
	parser = argparse.ArgumentParser(description="Simple ToDo Script.  Find me\
	    on GitHub.")
	parser.add_argument("command", type=str, choices=['add','remove','list'],
	    help="What needs to be accomplished.")
	parser.add_argument("option", type=str, nargs = '?', default = "", 
	    help = "Specify option for specific subcommand.")
	args = parser.parse_args()

	#Handle the input file
	with open('.todfile','r') as todfile:
		if args.command == 'add':
			addf(todfile,args.option,parser)
		elif args.command == 'remove':
			removef(todfile,args.option,parser)
		elif args.command == 'list':
			listf(todfile,args.option,parser)

if __name__ == '__main__':
	main()

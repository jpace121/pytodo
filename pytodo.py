#!/usr/bin/env python

import argparse

def addf(todfile,option,parser):
	if option:
		todfile.seek(0,2)
		todfile.write("* " + option + "\n")
	else:
		parser.print_help()

def donef(todfile,option,parser):
	return 0

def listf(todfile,option,parser):
	return 0

def main():
	#Parse all the input stuffs
	parser = argparse.ArgumentParser(description="Simple ToDo Script.  Find me\
	    on GitHub.")
	parser.add_argument("command", type=str, choices=['add','done','list'],
	    help="What needs to be accomplished.")
	parser.add_argument("option", type=str, default = "", 
	    help = "Specify option for specific subcommand.")
	args = parser.parse_args()

	#Handle the input file
	with open('.todfile','w+') as todfile:
		if args.command == 'add':
			addf(todfile,args.option,parser)
		elif args.command == 'done':
			donef(todfile,args.option,parser)
		elif args.command == 'list':
			listf(todfile,args.option,parser)

if __name__ == '__main__':
	main()

	

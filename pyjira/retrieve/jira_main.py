__author__ = 'Shiven'

import argparse
import jira_connect as jiracon
import jira_parse as jp

def start():
	parser = argparse.ArgumentParser()
	parser.add_argument("-u", "--url",  help="Url for the jira instance")
	parser.add_argument("-i", "--id", help="Enter the user id for the jira instance")
	parser.add_argument("-p", "--pwd", help="Enter the password for the jira instance")
	parser.add_argument("-prj", "--project", help="Enter the jira project name")
	parser.add_argument("-d", "--dir", help="Enter the directory where the issues need to be stored")
	args = parser.parse_args()
	if args.url and args.id and args.pwd and args.project:
	    jira = jiracon.connect(args.url, args.id, args.pwd)
	    if jira is not None:
	    	jp.parse(args.url, args.project, jira, args.dir, args.id, args.pwd)
	    else:
	    	print "Error occurred while connecting to jira. Please check the connection parameters"
	else:
	    parser.print_help()
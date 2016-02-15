__author__ = 'Shiven'

import argparse
#import jira_parse as jp
from jira_connect import Connect
from parse import Parse

def start():
	parser = argparse.ArgumentParser()
	parser.add_argument("-u", "--url",  help="Url for the jira instance")
	parser.add_argument("-i", "--id", help="Enter the user id for the jira instance")
	parser.add_argument("-p", "--pwd", help="Enter the password for the jira instance")
	parser.add_argument("-prj", "--project", help="Enter the jira project name")
	parser.add_argument("-d", "--dir", help="Enter the directory where the issues need to be stored")
	args = parser.parse_args()
	if args.url and args.id and args.pwd and args.project:
		conn = set_conn_info(args.url, args.id, args.pwd)
		jira = conn.connect()
		print "Connected"
		if jira is not None:
			parse = set_parser_info(jira, args.project, args.dir)
			parse.parse()
		else:
			print "Error occurred while connecting to jira. Please check the connection parameters"
	else:
		parser.print_help()

#Setting connection information in the Parse class
def set_parser_info(jira, prj, dirname):
	parse = Parse(prj, jira, dirname)
	return parse

#Setting connection info in the Connect class
def set_conn_info(url, user, pwd):
	Connect.url = url
	Connect.user = user
	Connect.pwd = pwd
	conn = Connect()
	return conn
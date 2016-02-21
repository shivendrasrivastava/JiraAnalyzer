__author__ = "Shiven"

import argparse
from connect import Connect
from parse import Parse
from file_manager import File
from loggerutil import simple_decorator, logger_main


class ArgParser(object):

	def __init__(self):
		logger_main.info(" Initializing ArgParser")

	#Parsing of arguments and calling connect and parse
	@simple_decorator
	def start(self):
		parser = argparse.ArgumentParser()
		parser.add_argument("-u", "--url",  help="Url for the jira instance")
		parser.add_argument("-i", "--id", help="Enter the user id for the jira instance")
		parser.add_argument("-p", "--pwd", help="Enter the password for the jira instance")
		parser.add_argument("-prj", "--project", help="Enter the jira project name")
		parser.add_argument("-d", "--dir", help="Enter the directory where the issues need to be stored")
		args = parser.parse_args()
		if args.url and args.id and args.pwd and args.project and args.dir:
			self.set_file_info(args.dir)
			conn = self.set_conn_info(args.url, args.id, args.pwd)
			jira = conn.connect_to_jira()
			if jira is not None:
				parse = self.set_parser_info(jira, args.project, args.dir)
				parse.parse()
			else:
				logger_main.error("Error occurred while connecting to jira. Please check the connection parameters")
		else:
			parser.print_help()

	#Setting connection information in the Parse class
	def set_parser_info(self,jira, prj, dirname):
		parse = Parse(prj, jira, dirname)
		return parse

	#Setting connection info in the Connect class
	def set_conn_info(self,url, user, pwd):
		Connect.url = url
		Connect.user = user
		Connect.pwd = pwd
		conn = Connect()
		return conn

	def set_file_info(self, dirname):
		File.dirname = dirname

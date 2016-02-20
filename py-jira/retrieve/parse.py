#class used for parsing data from jira
__author__ = "Shiven"
import json
from connect import Connect
from file_manager import File
from loggerutil import simple_decorator
from loggerutil import logger_parse
from pool import ConnectionPoolManager

class Parse(object):

	#Constructor to set initial values
	def __init__(self, prj_name, jira, dirname):
		logger_parse.info(" Initializing Parse ")
		self.prj = prj_name
		self.jira = jira
		self.dir= dirname
		self.file = File()
		self.conn = ConnectionPoolManager()

	#Method that starts the parsing
	@simple_decorator
	def parse(self):
		logger_parse.info("Parsing started....")
		self.file.create_dir_if_not_exist(self.dir)
		proj = self.jira.project(self.prj)
		issues_info = self.jira.search_issues(self.get_query_string(), maxResults=0, fields=['total'], json_result=True)
		logger_parse.info("Total no of issues are %s", str(issues_info['total']))
		total_no_of_issues = issues_info['total']
		self.retrieve(total_no_of_issues)

	#Forms the query string for the parser.
	def get_query_string(self):
		query_string = 'project='+self.prj
		return query_string

	@simple_decorator
	def retrieve(self, total_no_of_issues):
		start = 0
		count = 0
		while count < total_no_of_issues:
			issues = self.search(total_no_of_issues, start)
			logger_parse.info("Iterating over results now")
			if issues is not None:
				for key in issues:
					json_data = self.get_issue_detail(key)
					self.file.write_data_file(json_data, key)
					count += 1
					start = count
			else:
				logger_parse.info("No more issues to be parsed")
		logger_parse.info("Parsing complete")
		self.file.write_status_file(self.prj, count, total_no_of_issues)

	def get_rest_api_url(self, key):
		if not Connect.url:
			raise ValueError(" URL value is required ")
		return Connect.url + "/rest/api/latest/issue/" + str(key)


	def search(self, subset, start):
		key_field = 'key'
		issues = self.jira.search_issues(self.get_query_string(), maxResults=subset, startAt=start, fields=key_field)
		return issues

	#Gets issue details from
	def get_issue_detail(self, key):
		data = self.conn.get_issue_detail(key)
		#request = self.conn.get_http_request()
		#request_data = request('GET', self.get_rest_api_url(key))
		json_data = json.loads(data)
		formatted_data =  json.dumps(json_data, indent=4, sort_keys=True)
		return formatted_data
#class used for parsing data from jira
__author__ = "Shiven"
import json
import requests
from connect import Connect
from file_manager import File
from retrieve.loggerutil import simple_decorator

class Parse(object):

	#Constructor to set initial values
	def __init__(self, prj_name, jira, dirname):
		self.prj = prj_name
		self.jira = jira
		self.dir= dirname
		self.file = File()

	#Method that starts the parsing
	@simple_decorator
	def parse(self):
		print "Parsing started...."
		proj = self.jira.project(self.prj)
		issues_info = self.jira.search_issues(self.get_query_string(), maxResults=0, fields=['total'], json_result=True)
		print issues_info['total']
		total_no_of_issues = issues_info['total']
		self.retrieve(total_no_of_issues)

	#Forms the query string for the parser.
	def get_query_string(self):
		query_string = 'project='+self.prj
		return query_string

	@simple_decorator
	def retrieve(self, total_no_of_issues):
		issues = None
		if total_no_of_issues > 1000:
			subset = 1000
			start = 0
			no_of_issues = total_no_of_issues
			print "Issues being queried are ", no_of_issues
			while no_of_issues > 0:
				issues = self.search(subset, start)
				start = start + subset
				no_of_issues = no_of_issues - start
				print "Iterating over results now"
				if issues is not None:
					for key in issues:
						json_data = self.get_issue_detail(key)
						print "Writing file for issue ", key
						self.file.write_data_file(json_data, key)
				else:
					print "No issues to be parsed"
		else:
			print "Parsing issues... total issues are less than 1000"
			issues = self.search(total_no_of_issues, 0)
			if issues is not None:
				for key in issues:
					request_data = self.get_issue_detail(key)
					self.file.write_data_file(json_data, key)

		print "Parsing complete."
		self.file.write_status_file()

	def get_rest_api_url(self, key):
		if not Connect.url:
			raise ValueError(" URL value is required ")
		return Connect.url + "/rest/api/latest/issue/" + str(key)


	def search(self, subset, start):
		issues = self.jira.search_issues(self.get_query_string(), maxResults=subset, startAt=start)
		return issues

	#Gets issue details from
	def get_issue_detail(self, key):
		request_data = requests.get(self.get_rest_api_url(key), auth=(Connect.user, Connect.pwd))
		json_data = json.loads(request_data.text)
		return json_data
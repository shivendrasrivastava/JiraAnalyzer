#class used for parsing data from jira
import json
import requests
from jira_connect import Connect

class Parse(Connect):

	#Constructor to set initial values
	def __init__(self, prj_name, jira, dirname):
		self.prj = prj_name
		self.jira = jira
		self.dir= dirname

	#Method that starts the parsing
	def parse(self):
		print "Parsing started...."
		proj = self.jira.project(self.prj)
		issues_info = self.jira.search_issues(self.get_query_string(), maxResults=0, fields=['total'], json_result=True)
		print issues_info['total']
		total_no_of_issues = issues_info['total']
		self.retrieve(total_no_of_issues)

	def get_query_string(self):
		query_string = 'project='+self.prj
		return query_string

	def retrieve(self, total_no_of_issues):
		issues = None
		if total_no_of_issues > 1000:
			subset = 1000
			start = 0
			no_of_issues = total_no_of_issues
			print "Issues being queried are ", no_of_issues
			while no_of_issues > 0:
				print "Searching with ", no_of_issues
				print "Starting at ", start
				issues = self.search(subset, start)
				start = start + subset
				no_of_issues = no_of_issues - start
				print "Iterating over results now"
				if issues is not None:
					for key in issues:
						json_data = self.get_issue_detail(key)
						print "Writing file for issue ", key
						self.writeToFile(json_data, key)
				else:
					print "No issues to be parsed"
		else:
			print "Parsing issues... total issues are less than 1000"
			issues = self.search(total_no_of_issues, 0)
			if issues is not None:
				for key in issues:
					request_data = self.get_issue_detail(key)
					self.writeToFile(json_data, key)

		print "Parsing complete."

	def get_rest_api_url(self, key):
		return Connect.url + "/rest/api/latest/issue/" + str(key)

	def search(self, subset, start):
		issues = self.jira.search_issues(self.get_query_string(), maxResults=subset, startAt=start)
		return issues

	#Write issue data to file with name as the issue id
	def writeToFile(self, json_data, key):
		target = open(self.get_file_name(key), 'w')
		target.write(json.dumps(json_data, indent=4))
		target.close()

	def get_issue_detail(self, key):
		request_data = requests.get(self.get_rest_api_url(key), auth=(Connect.user, Connect.pwd))
		json_data = json.loads(request_data.text)
		return json_data

	def get_file_name(self, key):
		filename = self.dir + "/" + str(key)
		return filename


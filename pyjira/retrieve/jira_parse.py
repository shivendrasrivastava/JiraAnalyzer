__author__ = 'Shiven'
import json

def parse(prj_name, jira, dirname):
	print "Fetching project", prj_name
	proj = jira.project(prj_name)
	query_string = 'project='+prj_name
	issues_info = jira.search_issues(query_string, maxResults=0, fields=['total'], json_result=True)
	print issues_info['total']
	total_no_of_issues = issues_info['total']
	retrieve(total_no_of_issues, query_string, jira, dirname)

#Constructs the file name from the key
def getFileName(dirname, key):
	filename = dirname + "/" + str(key) + ".json"
	return filename

#Writes the issues to a file with the name as the issue name and json
def writeToFile(dirname, key):
	target = open(getFileName(dirname, key), 'w')
	target.write(json.dumps(key.raw, indent=4))
	target.close()

#Determine retrieval process for all the issues.
def retrieve(total_no_of_issues, query_string, jira, dirname):
	issues = None
	if total_no_of_issues > 1000:
		subset = 1000
		start = 0
		no_of_issues = total_no_of_issues
		print " Issues querying are ", subset
		while no_of_issues > 0:
			print "Searching with ", no_of_issues
			print "Starting at ", start
			issues =  search(query_string, subset, start, jira)
			start = start + subset 
			no_of_issues = no_of_issues - subset
			#jira.search_issues(query_string, maxResults=1000, startAt=0)
			print "Got the results"
			if issues is not None:
				for key in issues:
					print "Writing file for issue ", key
					writeToFile(dirname, key)
	else:
		issues = search(query_string, total_no_of_issues, 0, jira);
		if issues is not None:
			for key in issues:
				print "Writing file for issue ", key
				writeToFile(dirname, key)
			#print json.dumps(key.raw, indent=4)
			#

#Search the jira db using the query fields.
def search(query_string, max, start, jira):
	issues = jira.search_issues(query_string, maxResults=max, startAt=start)
	return issues


__author__ = 'Shiven'

from jira import JIRA

def connect(url, id, password):
	print "Connecting to a JIRA instance"
	jira = JIRA(url, basic_auth=(id, password))
	return jira




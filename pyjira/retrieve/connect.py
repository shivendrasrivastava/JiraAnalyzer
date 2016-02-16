__author__ = 'Shiven'

from jira import JIRA

class Connect(object):

	url = ""
	user = ""
	pwd = ""

	def __init__(self):
		print "Initialized Connect Class"

	def connect(self):
		print "Connecting to a JIRA instance"
		jira = JIRA(self.url, basic_auth=(self.user, self.pwd))
		return jira
__author__ = 'Shiven'

from jira import JIRA
from loggerutil import simple_decorator, logger_connect

class Connect(object):

	url = ""
	user = ""
	pwd = ""

	@simple_decorator
	def __init__(self):
		logger_connect.info(" Initializing Connect ")

	def connect_to_jira(self):
		jira = JIRA(self.url, basic_auth=(self.user, self.pwd))
		return jira
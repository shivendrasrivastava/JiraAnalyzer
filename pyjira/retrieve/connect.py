__author__ = 'Shiven'

from jira import JIRA
from retrieve.loggerutil import simple_decorator


class Connect(object):

	url = ""
	user = ""
	pwd = ""

	@simple_decorator
	def __init__(self):
		print ""

	def connect_to_jira(self):
		jira = JIRA(self.url, basic_auth=(self.user, self.pwd))
		return jira
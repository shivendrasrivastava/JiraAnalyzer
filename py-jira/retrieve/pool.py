__author__ = "Shiven"
from connect import Connect
import urllib3
import json
from loggerutil import simple_decorator, logger_connect

class ConnectionPoolManager(object):

	def __init__(self):
		logger_connect.info("Initializing ConnectionPoolManager ")
		self.http = urllib3.PoolManager(10)
		urllib3.disable_warnings()
		auth = str(Connect.user) + ":" + str(Connect.pwd)
		self.headers = urllib3.util.make_headers(basic_auth=auth)

	def get_http_request(self):
		return self.http

	def get_issue_detail(self, key):
		response = self.http.request('GET', Connect.url+"/rest/api/latest/issue/"+str(key), headers=self.headers)
		#response.read().decode('utf-8')
		return response.data.decode('utf-8')

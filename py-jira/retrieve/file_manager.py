__author__ = "Shiven"

import json
import datetime
from loggerutil import simple_decorator, logger_file
import os

class File(object):

	dirname = ""

	def __init__(self):
		logger_file.info("Initializing FileManager") 

	#Get file name from the issue id
	def get_file_name(self, key):
		filename = self.dirname + "/" + str(key)
		return filename

	#Constructs the file name for status file.
	def get_status_file_name(self):
		filename = self.dirname + "/" + "status.json"
		return filename

	# Write json data to file
	def write_data_file(self, json_data, key):
		target = open(self.get_file_name(key), 'w')
		#data = json.dumps(json_data, indent=4)
		#print data
		target.write(json_data)
		target.close()

	def write_status_file(self, key, count, total, error):
		logger_file.info("Writing status file")
		curr = datetime.datetime.now()
		target = open(self.get_status_file_name(), 'w')
		file_data = {}
		file_data['last_updated_time'] = str(curr)
		file_data['project'] = str(key)
		file_data['total_no_of_issues_parsed'] = str(count)
		file_data['total_no_of_issues'] = str(total)
		file_data['error'] = str(error)
		target.write(json.dumps(file_data, indent=4))
		target.close()

	def create_dir_if_not_exist(self, dirname):
		if not os.path.isdir(dirname):
			os.makedirs(dirname)

	def read_status_json_if_exists(self, dirname)
		if os.path.isdir(dirname):
			with open('status.json') as data_file:
				data = json.load(data_file)
				return data
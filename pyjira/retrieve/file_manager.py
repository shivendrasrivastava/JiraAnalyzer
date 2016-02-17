__author__ = "Shiven"

import json
import datetime
from retrieve.loggerutil import simple_decorator

class File(object):

	dirname = ""

	def __init__(self):
		print "Initializing FileManager"

	#Get file name from the issue id
	def get_file_name(self, key):
		filename = self.dirname + "/" + str(key)
		return filename

	#Constructs the file name for status file.
	def get_status_file_name(self):
		filename = self.dirname + "/" + "status.json"

	# Write json data to file
	def write_data_file(self, json_data, key):
		target = open(self.get_file_name(key), 'w')
		target.write(json.dumps(json_data, indent=4))
		target.close()

	def write_status_file(self):
		now = datetime.datetime.now()
		target = open(self.get_status_file_name(), 'w')
		target.write(json.dump({"last_updated_time" : now}))
		target.close()
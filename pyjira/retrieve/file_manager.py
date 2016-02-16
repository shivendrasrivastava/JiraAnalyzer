__author__ = "Shiven"

import json

class File(object):

	dirname = ""

	def __init__(self):
		print "Initializing FileManager"

	#Get file name from the issue id
	def get_file_name(self, key):
		filename = self.dirname + "/" + str(key)
		return filename

	# Write json data to file
	def write_to_file(self, json_data, key):
		target = open(self.get_file_name(key), 'w')
		target.write(json.dumps(json_data, indent=4))
		target.close()

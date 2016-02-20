import os
import stat


st = os.stat('extract.py')
if not bool(st.st_mode & stat.S_IEXEC):
	print "Setting permissions for extract.py"
	os.chmod('extract.py', st.st_mode | stat.S_IEXEC)
else:
	print "  "
	print "---------------------Permissions assigned for extract.py successfully--------------------"
	print "  "

st = os.stat('run.py')
if not bool(st.st_mode & stat.S_IEXEC):
	print "Setting permissions for run.py"
	os.chmod('run.py', st.st_mode | stat.S_IEXEC)
else:
	print "  "
	print "---------------------Permissions assigned for run.py successfully------------------------"
	print "  "


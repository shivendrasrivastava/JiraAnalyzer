import os
import stat

st = os.stat('extract.py')
os.chmod('extract.py', st.st_mode | stat.S_IEXEC)

st = os.stat('run.py')
os.chmod('run.py', st.st_mode | stat.S_IEXEC)


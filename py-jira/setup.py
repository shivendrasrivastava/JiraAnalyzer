#!bin/python
__author__ = "Shiven"

from setuptools import setup, find_packages

try:
	import pypandoc
	long_description = pypandoc.convert('JiraAnalyzer/README.md', 'rst')
except(IOError, ImportError):
	long_description = open('README.md').read()

with open('requirements.txt') as req_file:
	requirements = req_file.read().splitlines()

version = 1.0

setup(
	name = 'py-jira',
	version = version,
	install_requires = requirements,
	author = "Shivendra Srivastava",
	author_email = "mail2shivendra@gmail.com",
	packages = find_packages(),
	include_package_data = True,
	description = "Retrieves jira issues and stores them into mongo db",
	long_description = long_description,
	)

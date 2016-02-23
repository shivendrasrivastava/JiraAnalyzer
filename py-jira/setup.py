#!bin/python
__author__ = "Shiven"

from setuptools import setup, find_packages

try:
	import pypandoc
	long_description = pypandoc.convert('JiraAnalyzer/README.md', 'rst')
except(IOError, ImportError):
	long_description = "This is used to retrieve jira issues from the site and store it in mongodb"#open('README.md').read()

with open('requirements.txt') as req_file:
	requirements = req_file.read().splitlines()

version = 1.0

setup(
	name = 'py-jira',
	version = version,
	install_requires = ['certifi>=2015.11.20.1',
	'jira>=0.1.0',
	'oauthlib>=1.0.3',
	'requests>=2.9.1',
	'requests-oauthlib>=0.6.1',
	'requests-toolbelt>=0.6.0',
	'six>=1.10.0',
	'tlslite>=0.4.9',
	'urllib3>=1.14',
	'wheel>=0.24.0'],
	author = "Shivendra Srivastava",
	author_email = "mail2shivendra@gmail.com",
	packages = find_packages(),
	include_package_data = True,
	description = "Retrieves jira issues and stores them into mongo db",
	long_description = long_description,
    classifiers = [
    'Programming Language :: Python',
    'Development Status :: 3 - Alpha',
    'Natural Language :: English',
    'Environment :: Web Environment',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Topic :: Software Development :: Libraries :: Python Modules',
    'Topic :: Software Development :: Libraries :: Application Frameworks',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
	)

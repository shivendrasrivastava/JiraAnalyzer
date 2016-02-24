# JiraAnalyzer

### Requirement :-
  * Retreive project related information from JIRA
  * Analyze the issues based on KPIs 

### Usage :-
  * Ensure python, pip are installed on the system.
  * Clone this project
  * Run the setup.py script using the command "<code> python init.py </code>". This script will set required permission for the run.py file.
  * Run the file run.py with the option -h to get the usage params for this file.
  * Fetching issues :-
    * <code> python run.py -u _'url for the server'_<br>
                    -i _'username'_<br>
                    -p _'password'_<br> 
                    -prj _'project name'_<br>
                    -d _'directory name for issues'_<br> </code>

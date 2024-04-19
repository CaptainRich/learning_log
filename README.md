# $`\textcolor{blue}{\text{Learning Log}}`$
A script to build a web page (site) to track learning (through journaling).
Richard Ay (March 2024, *updated April 2024*)

## $`\textcolor{blue}{\text{Table of Contents}}`$
* [Setup](#setup)
* [Environment](#environment)
* [Usage](#Usage)
* [References](#references)
* [File List](#file-list)
* [Technologies and Imports](#Technologies-and-Imports)
* [Images](#Images)

## Setup

To use this program, activate the 'virtual environment' "ll_Env".  Then setup a
new Django project using the command: "django-admin start project ll_project .". 
NOTE the trailing '.' is IMPORTANT.  For additional details on manipulating Django
see the separate ".md" file https://github.com/CaptainRich/GitAPI/blob/main/django.md  

## Environment
A virtual environment is created so that the installation of matplotlib and plotly
remain local to this subdirectory, and do not affect the rest of the machine.

The virtual environment can be setup using the command: 
**'python -m venv "ll_env" --upgrade-deps --prompt="ll_env"'**

To start/stop the virtual environment, use the commands: **'ll_env\scripts\activate'** 
or **'deactivate'**. Once activated, the virtual environment will change the (terminal) 
prompt from (PS) to (ll_env).

After starting the virtual environment, django can be installed 
with the commands:  
**'python -m pip install django'**  
 

Subsequently the installations can be verified with the command:   
**'python -m pip show django'**  



## Usage
From VSCode, by issuing the command (note the suffix ".py' is required)  
- 'python manage.py runserver'   to start the Django server
- 'http://localhost:8000'        to start the browser at the home page 

 


## References
1. Python Crash Course, Eric Matthes, No Starch Press, 2023. Chapters 12-15.  


## File List


**/images** - a subdirectory with script images  


## Technologies and Imports
The following modules are necessary imports (imported in the .py files):  
- django
- django-bootstrap5
 

## Images
The images below show the resulting visualizations and status reports generated 
by the script:  

The 'Python' repository:  
![Python Repository](https://github.com/CaptainRich/GitAPI/blob/main/images/python_repos.png)  







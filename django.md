# $`\textcolor{blue}{\text{Django Implementation}}`$
This markup file details how to setup a Django project for Python.  
Richard Ay (April 2024, *updated April 2024*)  


## $`\textcolor{blue}{\text{Table of Contents}}`$
* [Setup](#setup)
* [Project and Database](#Project-and-Database)
* [Building and Starting the Application](#Building-and-Starting-the-Application)
* [Django Shell](#Django-Shell)


## Basic Setup
It is recommended that the project be setup with a virtual environment.  This is
so that any packages installed don't affect the entire machine.  A virtual 
environment can be setup and used with the following terminal commands.  

To create the virtual environment and change the terminal prompt:  
**'python -m venv "env_name" --upgrade-deps --prompt="env_name"'**  

To activate the virtual environment:  
**env_name\scripts\activate**  

To deactivate the virtual environment:  
**deactivate**  

Of course Django must be installed into the virtual environment.  This terminal
command can be used to install Django:  

**python -m pip install django**  

Subsequently the installations can be verified with the command:   
**'python -m pip show django'**  

================================================================================

## Project and Database
From within the virtual environment, the project can be created with the terminal
command:  

**django-admin startproject proj_name .**  

Note the trailing '.' is very important!  This '.' creates a directory structure 
that facilitates deployment of the application.

Django stores most project information in a database, therefore the database must 
be created.  The following terminal command will create and verify the initial
SQLite database:  

**python manage.py migrate**  

Anytime the database schema is changed (i.e. new models are added) Django must 
be made aware of the changes, so as to update the database. The following 
terminal commands are necessary to accomplish this change/update:  

**python manage.py makemigrations "app_name"**  
**python manage.py migrate**  

The application (project) must run in a server.  The server also checks to make 
sure the project is setup properly.  The following terminal command will
start the (local) server at http://127.0.0.1:8000/ or http://localhost:8000. Note
this assumes the local environment has been activated!

**python manage.py runserver**  

This server should remain running for future development and local usage of the
application.


================================================================================

## Building and Starting the Application
Leave the development server running and open a new terminal window.  In this new
terminal, activate the local environment, then start a new application by issuing
 the terminal command:  

**python manage.py startapp "app_name"**   

This command creates a new subdirectory for the application 'app_name'.  (A Django  
project is actually a group of applications that work together. Each application 
will have .py files for: models, admin, and view.)

A 'superuser' must be created who has all privileges.  The following terminal
command should be issued to setup the 'superuser':  

**python manage.py createsuperuser**  

Then follow the prompts to finish setting up the 'superuser'.


================================================================================

## Django Shell
Django supports an interactive terminal - a shell, similar to the Python shell
IDLE.  The following terminal command invokes the shell:

**python manage.py shell**

From within this 'shell', python/django statements can be issued to test and/or
troubleshoot the application.  To exit the shell, issue the CRTL-Z key combination.   


================================================================================

## Installed Apps
A Django project is a collection of applications.  All applications must be listed in 
the main 'settings.py' file.  The applications should be separated into (appropriately
commented) groups: 'my project apps', '3rd party apps', 'default django apps'.

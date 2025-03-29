# Edu-Blog
### Blog Web App System

Welcome aboard to our web application system version 1.0
We hereby provide docs and resources on how to maneuver through the whole system
From Signing up for the platform to signing in to reading and updating your blogs/content, we've made it easy for you to interact with our friendly user interface.

Our platform is built on Django

Since its still in testing mode, if you want to check it out then we will provide instructions on how to do so.

---------------------------------------------------------------------------------------------------------------------

## Cloning the repository
# via HTTPS: 
`https://github.com/devharnold/Edu-Blog.git`

# via SSH: 
`git@github.com:devharnold/Edu-Blog.git`

# via github cli: 
`gh repo clone devharnold/Edu-Blog`

## Downloading dependencies on your project directory
First you need to initialize a python virtual environment:
**On windows CMD or powershell:**
Navigate to your project directory: `cd path\to\your\project`
Create a virtual environment: `python -m venv venv`
Activate the virtual environment:
Comand Prompt (CMD): `venv\Scripts\activate`
Powershell: `venv\Scripts\Activate.ps1`
*If you get an execution policy error, run: Set-ExecutionPolicy Unrestricted -Scope Process before activating.*

**On Linux Terminal:**
Navigate to your project directory: `cd /path/to/your/project`
Create a virtual environment: `python3 -m venv venv` *Ensure you have `python3` installed*
Activate the virtual environment: `source venv/bin/activate`
To deactivate on both Operating Systems, you just `deactivate`

**Installing Django:**
`pip install Django`

**Running the server:**
`python3 manage.py runserver`
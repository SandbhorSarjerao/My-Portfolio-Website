# My-Portfolio-Website

This is My Portfolio Website , I developed it using Python language.
For developling it I used Flask Framework.

# Technology used -
1) Python 
2) FLASK Framework - pip install Flask
3) HTML - defined Content & Text - use HTML to display information for the visitor/on the web browser.
4) CSS - Styling of Website
5) JS - Actions

# Key-Points =>
1) Server.py is the Python main file, to handle HTTP requests. Use this file to run FLASK as FLASK_APP=Server.py
2) Keep all .html files in "Templates" folder
3) Keep all .css, .js & image files in "Static" folder
4) Create ENV folder by below command
   - cd project-folder
   - python -m venv ./                 => virtual environment to manage the dependencies for this project

# Steps to Run =>
1) execute ".\Scripts\activate.bat" file	=> To activate your programming environment
   If below error =
         Error => Activate.ps1 cannot be loaded because running scripts is disabled on this system.
   Then execute below command =>  
         Set-ExecutionPolicy Restricted     or    "Set-ExecutionPolicy RemoteSigned -Scope CurrentUser"
2) execute below commands from Project Terminal =>
    set FLASK_ENV=development  => for Development environment
    set FLASK_APP=Server.py
    flask run       or      flask run -p 5001      or       python -m flask run

# Server IP Address & Port =>
http://127.0.0.1:5000/

# About FLASK Framework =>
Flask is a small and lightweight Python web framework that provides useful tools and features that make creating web applications in Python easier. It gives developers flexibility and is a more accessible framework for new developers since you can build a web application quickly using only a single Python file. Flask is also extensible and doesn’t force a particular directory structure.

Within the activated environment, By using below pip command we can install Flask =>
 pip install flaskor
http://localhost:5000/

Press CTRL+C to quit

# Document Reference =>
1) https://xkcd.com/
2) www.mashup-template.com/
3) https://flask.palletsprojects.com/en/2.0.x/installation/
4) https://flask.palletsprojects.com/en/2.0.x/quickstart/	
5) https://www.digitalocean.com/community/tutorials/how-to-make-a-web-application-using-flask-in-python-3
6) https://docs.python.org/3/library/csv.html

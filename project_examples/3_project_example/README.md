# Project Name

## Project Overview

## Web Link

## Application File Layout

    .
    ├── app
    │   ├── __init__.py                      # Flask file that runs app
    │   ├── views.py                         # Flask file that contains endpoints
    │   ├── models
    │   │   └── classifier.pkl               # Pickle file of model  
    │   └── templates   
    │       ├── go.html                      # Classification result page of web app
    │       └── master.html                  # Main page of web app    
    ├── models  
    │   └── classifier.pkl                   # Pickle file of model  
    ├── README.md
    ├── Procfile                             # Specifies commands executed on startup
    ├── run.py                               # Entry point for the application
    └── requirements.txt                     # List of libraries to be installed

## Instructions (Skip steps 2 and 3 if .pkl file and .db database exists):
1. Run the following command to install necessary libraries. (Make sure to `pip uninstall scikit-learn` before to avoid compattability issues)
    `pip install -r requirements.txt`

2. Run the following command in the app's directory to run the web app.
    `gunicorn run:app`

3. Go to http://127.0.0.1:8000


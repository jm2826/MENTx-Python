# Project Name

## Project Overview

## Web Link


## Application File Layout

    .
    ├── app
    │   ├── __init__.py                      # Flask file that runs app
    │   ├── views.py                         # Flask file that contains endpoints
    │   ├── data
    │   │   └── house.db                     # Database for House data
    │   ├── models
    │   │   └── classifier.pkl               # Pickle file of model  
    │   └── templates   
    │       ├── go.html                      # Classification result page of web app
    │       └── master.html                  # Main page of web app    
    ├── setup                   
    │   ├── train_classifier.py              # Train ML model
    │   └── process_data.py                  # Data cleaning
    ├── models
    │   ├── train_classifier.py              # Train ML model      
    │   └── classifier.pkl                   # Pickle file of model  
    ├── README.md
    ├── Procfile                             # Specifies commands executed on startup
    ├── run.py                               # Entry point for the application
    └── requirements.txt                     # List of libraries to be installed

## Instructions (Skip steps 2 and 3 if .pkl file and .db database exists):
1. Run the following command to install necessary libraries.
    `pip install -r requirements.txt`

2. Run the following commands in the project's root directory to create the database and model.

    - To run ETL pipeline that cleans data and stores in database
        `python setup/process_data.py setup/house.csv app/data/house.db`
    - To run ML pipeline that trains classifier and saves
        `python setup/train_classifier.py app/data/house.db app/models/classifier.pkl`

3. Run the following command in the app's directory to run the web app.
    `gunicorn run:app`

4. Go to http://127.0.0.1:8000

## Example

## Summary

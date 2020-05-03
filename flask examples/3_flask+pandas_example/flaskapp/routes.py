from flaskapp import app
from flask import render_template
import pandas as pd
from wrangling_scripts.wrangling import data_wrangling

data, df = data_wrangling()

print(data)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', tables=[df.to_html(classes='data', header="true")])
    
@app.route('/project-one')
def project_one():
    return render_template('project_one.html')
    
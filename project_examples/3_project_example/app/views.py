import json
import pandas as pd
import re

from app import app, model
from flask import render_template, request, jsonify


# index webpage displays cool visuals and receives user input text for model
@app.route('/')
@app.route('/index')
def index():
    
    # render web page with plotly graphs
    return render_template('master.html')


# web page that handles user query and displays model results
@app.route('/go')
def go():
    # save user input in query
    age = int(request.args.get('age', ''))
    ward = int(request.args.get('ward', ''))
    semi = int(request.args.get('semi', ''))
    intensive = int(request.args.get('intensive', ''))

    response_list = [age, ward, semi, intensive]

    # Create empty dictionary to be used to create DataFrame
    df_dict = {}

    # List column features
    cols = ['Patient age quantile','Patient addmited to regular ward (1=yes, 0=no)','Patient addmited to semi-intensive unit (1=yes, 0=no)','Patient addmited to intensive care unit (1=yes, 0=no)']
    
    # zip puts two lists side by side
    for l, c in zip(response_list, cols):
        df_dict[c] = [l]

    query_df = pd.DataFrame(df_dict)

    print(model.predict(query_df))

    # use model to predict classification for query
    classification_label = model.predict(query_df)[0]

    # This will render the go.html Please see that file. 
    return render_template(
        'go.html',
        query=f"Age: {age} , Admitted to ward: {ward} , Admitted to semi-intensive unit: {semi} , Admitted to intensive care unit: {intensive}",
        classification_result={"result": classification_label}
    )
import json
import plotly
import pandas as pd
import re

from app import app, df, model
from flask import render_template, request, jsonify
from plotly.graph_objs import Bar


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
    query = request.args.get('query', '')

    query_df = pd.DataFrame({"LotArea":[query]})

    print(model.predict(query_df))

    # use model to predict classification for query
    classification_label = model.predict(query_df)[0]

    # This will render the go.html Please see that file. 
    return render_template(
        'go.html',
        query=query,
        classification_result={"result": classification_label}
    )
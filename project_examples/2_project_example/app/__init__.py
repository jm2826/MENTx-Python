import os
import pandas as pd

from flask import Flask
from sqlalchemy import create_engine
from joblib import load

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))

# load database engine
engine = create_engine('sqlite:///' + os.path.join(basedir, 'data/house.db'))

# load data
df = pd.read_sql_table('prices', engine)

# load model
model = load(os.path.join(basedir, "models/classifier.pkl"))

from app import views
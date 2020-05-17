import os
import pandas as pd

from flask import Flask
from joblib import load

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))

# load model
model = load(os.path.join(basedir, "models/classifier.pkl"))

from app import views
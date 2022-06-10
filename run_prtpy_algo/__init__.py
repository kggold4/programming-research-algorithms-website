import os
import sys

from flask import Flask, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
sys.path.append('/home/kggold4/prtpy')

from run_prtpy_algo import routes

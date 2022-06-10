import os
import sys

from flask import Flask, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
sys.path.append('../prtpy')

from prtpy.partitioning.kk import kk
from prtpy.partitioning.ckk import ckk
from prtpy.partitioning.rnp import rnp
from prtpy.partitioning.irnp import irnp
from run_prtpy_algo import routes

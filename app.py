from flask import Flask, render_template,request,redirect,session, abort, flash
from flask_cors import CORS, cross_origin
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

#import pdb; pdb.set_trace()
app = Flask(__name__)

app.config.from_pyfile('config.py')

db = SQLAlchemy(app)
ma = Marshmallow(app)
CORS(app)

from views import *

if __name__ == '__main__':
    app.run(port=5002)

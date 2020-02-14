from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
## engine = sa.create_engine('mssql+pyodbc://DESKTOP-FQPDNGK\SQLEXPRESS/database')
## engine = app.create_engine('mssql+pyodbc://user:password@server/database')
app.config['SQLALCHEMY_DATABAE_URI'] = 'sqlite:///storage.db'
db = SQLAlchemy(app)

from app.controllers import default

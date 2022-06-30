import os
import re  # regular expression package for python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
if os.path.exists("env.py"):  
    import env  # as this is in the ignore file, file needs to be found to be imported

# environment variables
app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")   

if os.environ.get("DEVELOPMENT") == "True":
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")
else:
    uri = os.environ.get("DATABASE_URL")  # get uri from heroku
    if uri.startswitch("postgres://"):
        uri = uri.replace("postgres://", "postgresql://", 1)
    app.config["SQLALCHEMY_DATABASE_URI"] = uri  # heroku

    
# instance import sqlalchemy class, set to instance of flask app
db = SQLAlchemy(app)

# needs to be imported after the above
from taskmanager import routes  # noqa

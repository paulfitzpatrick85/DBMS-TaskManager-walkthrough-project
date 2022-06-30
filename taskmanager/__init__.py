import os
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
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
# instance import sqlalchemy class, set to instance of flask app
db = SQLAlchemy(app)

# needs to be imported after the above
from taskmanager import routes  # noqa

from flask import render_template, request, redirect, url_for
from taskmanager import app, db
from taskmanager.models import Category, Task


@app.route("/")
def home():
    return render_template("tasks.html")


# populate category template in base.html
@app.route("/categories")
def categories():
    return render_template("categories.html")


@app.route("/add_category", methods=["GET", "POST"])   
def add_category():
    if request.method == "POST":
        category = Category  # set to new instance of Category from top of page
    return render_template("add_category.html")
# Methods used for form submission to db
# user clicks add_category in add_category.html, which calles this function
# funct then renders template which is a form, GET is used to 'get' the page
# post lets user submit form




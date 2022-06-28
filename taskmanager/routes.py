from flask import render_template, request, redirect, url_for
from taskmanager import app, db
from taskmanager.models import Category, Task


@app.route("/")
def home():
    return render_template("tasks.html")


# populate category template in base.html
@app.route("/categories")
def categories():
    categories = list(Category.query.order_by(Category.category_name).all())
    return render_template("categories.html", categories=categories)
# 1st categories refers to categorie.html
# 2nd categories refers to variable above


@app.route("/add_category", methods=["GET", "POST"])   
def add_category():
    if request.method == "POST":
        # set to new instance of Category from top of page
        category = Category(category_name=request.form.get("category_name"))  
        db.session.add(category)
        db.session.commit()
        return redirect(url_for("categories"))
    return render_template("add_category.html")
# Methods used for form submission to db
# user clicks add_category in add_category.html, which calles this function
# funct then renders template which is a form, GET is used to 'get' the page
# post lets user submit form




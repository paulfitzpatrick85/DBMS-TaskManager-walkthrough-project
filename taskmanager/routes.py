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


@app.route("/add_category", methods=["GET", "POST"])   # Methods used for form submission to db
def add_category(): 
    if request.method == "POST":
        # set to new instance of Category from top of page
        category = Category(category_name=request.form.get("category_name"))  
        db.session.add(category)
        db.session.commit()
        return redirect(url_for("categories"))
    return render_template("add_category.html")
# user clicks add_category in add_category.html, which calles this function
# funct then renders template which is a form, GET is used to 'get' the page
# post lets user submit form


# variable passed into python funct must be wrapped in ang brackets
@app.route("/edit_category/<int:category_id>", methods=["GET", "POST"])  
def edit_category(category_id):
    category = Category.query.get_or_404(category_id)  # querys db for specified record using data provided
    if request.method == "POST":  
        category.category_name = request.form.get("category_name")
        db.session.commit()
        return redirect(url_for("categories"))  # after category is edited, user is brought back to categories page
    return render_template("edit_category.html", category=category)


@app.route("/delete_category/<int:category_id>")  # cast as integer
def delete_category(category_id):
    category = Category.query.get_or_404(category_id)  # querys db for specified record using data provided or throw error page
    db.session.delete(category)
    db.session.commit()
    return redirect(url_for("categories"))
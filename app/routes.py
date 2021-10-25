from werkzeug.wrappers import request
from app import app, db
from flask import render_template, redirect, request
from app.models import Product
from app.forms import ProductForm

@app.route('/index', methods=['GET', 'POST'])
def index():
    products = Product.query.all()
    return render_template('index.html', products=products)

@app.route('/add-product', methods=['GET', 'POST'])
def add_product():
    form = ProductForm()
    if form.validate_on_submit():
        product = Product( 
            product_name = request.form["product_name"],
            product_desc = request.form["product_desc"],
            qty_stock = request.form.get("qty_stock"),
            price = request.form.get("price"),
            on_hand = request.form.get("on_hand")
        )
        print('valid')
        db.session.add(product)
        db.session.commit()
    return render_template('add_product.html', form=form)
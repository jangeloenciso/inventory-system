from app import app, db
from flask import render_template, redirect
from app.models import Product
from app.forms import ProductForm

@app.route('/index', methods=['GET', 'POST'])
def index():
    form = ProductForm()
    if form.validate_on_submit():
        product = Product(
            product_name = form.product_name.data,
            product_desc = form.product_desc.data,
            qty_stock = form.qty_stock,
            price = form.price.data,
            on_hand = form.on_hand
        )
        db.session.add(product)
        db.session.commit()
    products = Product.query.all()
    return render_template('index.html', form=form, products=products)
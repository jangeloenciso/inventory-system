from typing import Text
from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.fields.core import FloatField, IntegerField
from wtforms.validators import DataRequired
from app.models import Product

class ProductUpdateForm(FlaskForm):
    product_name = StringField('Product Name', validators=[DataRequired()])
    product_desc = TextAreaField('Product Description')
    qty_stock = IntegerField("Stock Quantity")
    price = FloatField("Price")
    on_hand = IntegerField("On hand quantity")
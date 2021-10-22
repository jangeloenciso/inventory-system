from enum import unique
from app import db, app

class Product(db.Model):
    __tablename__ = "products"
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(200))
    product_desc = db.Column(db.String(200))
    qty_stock = db.Column(db.Integer)
    price = db.Column(db.Integer)
    on_hand = db.Column(db.Integer)

    def __init__(self, product):
        self.product = product

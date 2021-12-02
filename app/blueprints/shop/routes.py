from stripe.api_resources import line_item, product
from werkzeug.utils import redirect
from .import bp as shop
from flask import render_template, redirect, url_for, flash, current_app as app
from .models import Product, Cart
import stripe
from flask_login import current_user
from app import db

@shop.route('/')
def index():
    stripe.api_key = app.config.get('STRIPE_TEST_SK')
    # print(stripe.api_key)
    context = {
        'products' : stripe.Product.list()
    }
    return render_template('shop/index.html', **context)

@shop.route('/product/add/<id>')
def add_product(id):
    print(id)
    cart_item = Cart.query.filter_by(product_key=str(id)).filter_by(user_id=current_user.get_id()).first()
    if cart_item:
        cart_item.quantity += 1
        db.session.commit()
        flash('Product added successfully', 'success')
        return redirect(url_for('shop.index'))
    cart_item = Cart(product_key=id, user_id=current_user.get_id(), quantity=1)
    db.session.add(cart_item)
    db.session.commit()

@shop.route('/cart')
def cart():
    stripe.api_key = app.config.get('STRIPE_TEST_SK')
    cart_items = []
    for i in Cart.query.filter_by(user_id=current_user.get_id()).all():
        stripe_product = stripe.Product.retrieve(i.product_key)
        product_dict = {
            'product' : stripe_product,
            'price' : float(stripe.Price.retrieve(stripe_product['metadata']['price_id'])['unit_amount']) / 100,
            'quantity' : i.quantity
        }
        cart_items.append(product_dict)
    context = {
        'cart' : cart_items
    }
    return render_template('shop/cart.html', **context)

@shop.route('/checkout', methods=['POST'])
def create_checkout_session():
    stripe.api_key = app.config.get('STRIPE_TEST_SK')
    items = [
        # {
        #     # Provide the exact Price ID (e.g. pr_1234) of the product you want to sell
        #     'price': 'price_1K26mIIGBbvkCxLnFjv7dhfy',
        #     'quantity': 2,
        # }
    ]

    for i in Cart.query.filter_by(user_id=current_user.get_id()).all():
        stripe_product = stripe.Product.retrieve(i.product_key)
        product_dict = {
            'price' : stripe.Price.retrieve(stripe_product['metadata']['price_id']),
            'quantity' : i.quantity
        }
        items.append(product_dict)

    try:
        checkout_session = stripe.checkout.Session.create(
            line_items=items,
            mode='payment',
            success_url='http://localhost:5000/',
            cancel_url='http://localhost:5000/'

        )
    except Exception as error:
        return str(error)
    return redirect(checkout_session.url, code=303)
from flask import request, Blueprint, session, jsonify
from datetime import datetime
import os
from DataBase.connection import DBConnection
from sql_provider import SQLProvider
from auth.routes import db_config

sql_provider = SQLProvider(os.path.join(os.path.dirname(__file__), 'sql'))
cart_blueprint = Blueprint('cart_bp', __name__, template_folder='templates')

@cart_blueprint.route('/<login>', methods = ['PUT', 'POST', 'GET'])
def report_post(login):
    cart_key = f"cart:{session['user_id']}"
    if request.method == 'POST':
        input_data = request.json
        print(input_data)
        product_id = input_data['prod_id']
        if cart_key not in session:
            session[cart_key] = {}
        cart = session[cart_key]
        if product_id in cart:
            if input_data['quantity'] == 0:
                cart.pop(product_id, None)
            else:
                cart[product_id]['quantity'] = input_data['quantity']
        else:
            cart[product_id] = {
                'prod_measure': input_data['prod_measure'],
                'quantity': input_data['quantity'],
                'prod_price': input_data['prod_price'],
                'prod_name': input_data['prod_name'],
                'prod_id': product_id
            }
        print(cart)
        session[cart_key] = cart
        return jsonify(list(session[cart_key].values()))
    elif request.method == 'PUT':
        with DBConnection(db_config) as cursor:
            sale_date = datetime.now().date()
            user_id = session['user_id']
            cursor.execute(sql_provider.get('salesInsert.sql', sale_date=sale_date, user_id=user_id))
            sale_id = cursor.lastrowid
            for prod_id, prod_info in session[cart_key].items():
                cursor.execute(sql_provider.get('productInsert.sql',
                                                           sale_id=sale_id,
                                                           prod_id=prod_id,
                                                           prod_price=prod_info['prod_price'],
                                                           quantity=prod_info['quantity']))
            cursor.close()
            print(session)
            session.pop(cart_key)
            print(session)
            return jsonify({'report': 'ok'})
    else:
        if cart_key in session:
            session.pop(cart_key)
        return jsonify({'report': 'ok'})

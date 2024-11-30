from flask import render_template, request, Blueprint, session, jsonify
import os
from DataBase.select import select_from_db
from sql_provider import SQLProvider
from auth.routes import db_config

sql_provider = SQLProvider(os.path.join(os.path.dirname(__file__), 'sql'))
spmkt_blueprint = Blueprint('spmk_bp', __name__, template_folder='templates')

@spmkt_blueprint.route('/<login>', methods = ['GET', 'POST'])
def supermarket_get(login):
    if (session['user_group'] == 'user'):
        if request.method == "GET":
            products = select_from_db(db_config, sql_provider.get('AllProducts.sql'))
            return render_template('supermarket.html', products=products, login=login)
        else:
            input_data = request.form
            products = select_from_db(db_config, sql_provider.get('product.sql', prod_name=input_data['prod_name']))
            return jsonify({'products': products})
    elif (session['user_group'] == 'manager'):
        if request.method == "GET":
            sales = select_from_db(db_config, sql_provider.get('AllSales.sql'))
            return render_template('manager.html', login=login, sales=sales)
        else:
            input_data = request.form['date']
            [day, month, year] = input_data.split('.', 3)
            sales = select_from_db(db_config, sql_provider.get('sales.sql', year=year[0:4], month=month, day=day))
            return jsonify({'sales': sales, 'day': day, 'month': month, 'year': year})
    elif (session['user_group'] == 'admin'):
        if request.method == "GET":
            return render_template('admin.html', login=login)
        else:
            input_data = request.form['date']
            [day, month, year] = input_data.split('.', 3)
            routes = select_from_db(db_config, sql_provider.get('routes.sql', year=year[0:4], month=month, day=day))
            return jsonify({'routes': routes})
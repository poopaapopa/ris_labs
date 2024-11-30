from flask import request, Blueprint, jsonify
import os
from DataBase.select import select_from_db
from sql_provider import SQLProvider
from auth.routes import db_config

sql_provider = SQLProvider(os.path.join(os.path.dirname(__file__), 'sql'))
manager_blueprint = Blueprint('manager_bp', __name__, template_folder='templates')

@manager_blueprint.route('/<login>', methods = ['PUT', 'POST'])
def report_post(login):
    input_data = request.form['date']
    [month, year] = input_data.split('.', 2)
    report_check = select_from_db(db_config, sql_provider.get('checkReport.sql', year=year[0:4], month=month))
    if request.method == 'PUT':
        return jsonify({'report': report_check})
    if request.method == 'POST':
        if not report_check:
            select_from_db(db_config, sql_provider.get('callReport.sql', year=year[0:4], month=month))
            report_check = select_from_db(db_config, sql_provider.get('checkReport.sql', year=year[0:4], month=month))
            return jsonify({'report': report_check})
        else:
            return jsonify({'report': [], 'month': month, 'year': year})
from flask import render_template, Flask, redirect, session
from auth.routes import auth_blueprint
from auth.acess import login_required
from supermarket.supermarket import spmkt_blueprint
from repCreating.managers import manager_blueprint
from cart.cart import cart_blueprint

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.register_blueprint(auth_blueprint, url_prefix=('/auth'))
app.register_blueprint(spmkt_blueprint, url_prefix=('/supermarket'))
app.register_blueprint(manager_blueprint, url_prefix=('/manager'))
app.register_blueprint(cart_blueprint, url_prefix=('/cart'))
app.secret_key = 'you_will_never_guess'

@app.route('/')
@login_required
def hello():
    return render_template('startpage.html')

@app.route('/counter')
def counter_handler():
    current_counter = session.get('counter', 0)
    current_counter += 1
    session['counter'] = current_counter
    session.permanent = True
    return str(session['counter'])

@app.route('/static')
def static_html():
    languages = ['c++', 'python', 'java', 'javascript']
    name = 'Dima'
    return render_template('index.html', languages=languages, name=name)

@app.route('/btst')
def btst_handler():
    return render_template('btst.html')

@app.route("/logout")
def exit():
    session.clear()
    return redirect("/")

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5001)
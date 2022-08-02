# Python script implementing the server side of
# the Womens Colthing webpage site.
# Flask webframe work used 

from flask import Flask
from flask import render_template
from flask import request, redirect, url_for
from flask import session
from werkzeug.security import generate_password_hash, check_password_hash
import json

from mongita import MongitaClientDisk

app = Flask(__name__)
app.secret_key=")(n27=smi+_+_n8ye[i2hjfs}{>.m269f"


# __GLOBALLY_DEFINED__
db_server = MongitaClientDisk(host="./.mongita")


# homepage endpoint routes and functions here
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/')
@app.route("/homepage")
def homepage():
    if 'username' in session:
        username = session['username']
        return render_template('homepage.html', user=username)
    return render_template('homepage.html')

@app.route("/homepage", methods=["GET"])
def get_homepage():
    if 'username' in session:
        username = session['username']
        return render_template('homepage.html', user=username)
    return redirect(url_for('get_login'))




# login endpoint routes and functions here
@app.route("/login")
def login():
    return render_template('login.html')
    # return render_template('create-acc.html')

@app.route("/login", methods=['GET'])
def get_login():
    if 'username' in session:
        return redirect(url_for('homepage'))
    return render_template('create-acc.html')

@app.route("/login", methods=['POST'])
def post_login():
    username = request.form.get("username", None)
    if username == None:
        return redirect(url_for('login'))
    try:
        with open(f"storage/{username}.json", "r") as f:
            creds = json.load(f)
    except Exception as e:
        print(f"Error in reading credentials. {e}")
        return redirect(url_for('login'))
    password = request.form.get("password", None)
    if not check_password_hash(creds['password'], password):
        print(f"Error - illegal password.")
        return redirect(url_for('login'))
    session['username'] = username
    return redirect(url_for('homepage'))




# create new account endpoint routes and functions here
@app.route("/create-new-acc", methods=['GET'])
def get_create_new_acc():
    if 'username' in session:
        return redirect(url_for('login'))
    return render_template('create-new-acc.html')

@app.route("/create-new-acc", methods=['POST'])
def post_create_new_acc():
    # assign username obj to return value of
    username = request.form.get("username", None)
    # logic to ensure legal username value
    if username == None:
        return redirect(url_for('get_create_new_acc'))
    for c in username.lower():
        if not(c.isalpha() or c.isdigit() or (c in '.-_')):
            print("Illegal charecter used")
            return redirect(url_for('get_create_new_acc'))
    
    # assign password obj to return value of   
    password = request.form.get("password", None)
    # logic to ensure legal password value
    if password == None:
        return redirect(url_for('get_create_new_acc'))
    if len(password) < 8:
        print("Password must be at leatst 8 characters")
        return redirect(url_for('get_create_new_acc'))
    repeated = request.form.get("repeated", None)
    if repeated == None:
        return redirect(url_for('get_create_new_acc'))
    if repeated != password:
        print("Passwords must match")
        return redirect(url_for('get_create_new_acc'))
    
    # a legal usename and password should exist
    # ensure there is not an account with these values already
    try:
        with open(f"storage/{username}.json", "r") as f:
            creds = json.load(f)
            print("Account username already exists")
            return redirect(url_for('login'))
    except Exception as e:
        pass

    # TODO: store the user credentials
    creds = {
        "username":username,
        "password":generate_password_hash(password)
    }
    with open(f"storage/{username}.json","w") as f:
        json.dump(creds, f)

    # return the logged-in user to a session
    session['username'] = username
    return redirect(url_for('login'))




# product page endpoint route and functions here
@app.route("/products-page")
def products_page():
    if 'username' in session:
        username = session['username']
    else:
        return render_template('products-page.html')
    return render_template('products-page.html', user=username)

@app.route("/products-page", methods=["GET"])
def get_products_page():
    if 'username' in session:
        username = session['username']
    else:
        return render_template('products-page.html')
    return render_template('products-page.html', user=username)

# _GLOBALLY_DEFINED_
# server_db = MongitaClientDisk(host="./.mongita")
#
# Approach: get request sent back from
# html form, insert item data into 
@app.route("/products-page", methods=["POST"])
def add_to_cart():
    if 'username' in session:
        username = session['username']
        items = []
        items.append((
            request.form.get('name')
        ))
        print(items)
        col_users = db_server["users"] # collection named "users" storing user data
        cart = col_users["cart"]
        cart.insert_one({'product':items})
            
         # products: ["<name>"],,, request.form.get("name")
    else:
        # add a pop alert to the user that they must be loged
        # in to add an item to a cart
        return render_template('products-page.html')
    return render_template('products-page.html', user=username)



@app.route("/checkout", methods=['GET', 'POST'])
def checkout():
    if 'username' in session:
        username = session['username']
    else:
        return redirect(url_for('login'))
    return render_template('checkout.html', user=username)
def post_checkout():
    if 'username' in session:
        username = session['username']
    else:
        return redirect(url_for('login'))
    return render_template('checkout.html', user=username)


@app.route("/logout", methods=['GET'])
def logout():
    session.pop('username', None) 
    return render_template('logout.html')


from flask import Flask, url_for
from flask import render_template
# to render template routes
from flask import request, redirect, url_for
# renders requests

# Flask includs a web server

app = Flask(__name__)

# decorator used
# route specifer returns computational recource
# -- returns index route --
@app.route("/")
def get_index():
    return "<p>Andreas web page</p>"

# data injection from a template
@app.route("/welcome")
def get_welcome():
    return render_template('welcome.html', name="Andreas")

@app.route("/santa")
def get_santa():
    print(dict(request.args))
    return render_template('welcome.html', name="Santa")

@app.route("/hi")
@app.route("/hi/")
@app.route("/hi/<name>")
def get_hi(name="Jon"):
    return render_template('welcome.html', name=name)

@app.route("/login", method=['GET'])
def get_login():
    return render_template('login.html')

@app.route("/login", methods=['POST'])
def get_login():
    username = request.form.get("username", "<missing name>")
    password = request.form.get("password", "<missing password>")
    if password == "password":
        return redirect(url_for('get_hi', name=username))
    else:
        return render_template('get_login')

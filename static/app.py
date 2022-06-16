from flask import Flask
from flask import render_template

# web server from Flask

app = Flask(__name__)

# decorator used
# route specifer returns computational recource
# -- returns index route --
@app.route("/")
def get_index():
    return "<p>Andreas web page</p>"

# 
# data injection from a template
@app.route("/welcome")
def get_welcome():
    return render_template('welcome.html', name="Andreas")

@app.route("/welcome")
def get_santa():
    return render_template('welcome.html', name="Santa")

@.route("/hi/abc")
def get_hi():
    return render_template('welcome.html', name="Jon")

from flask import Flask

# web server from Flask

app = Flash(__name__)

# decorator used
# route specifer returns computational recource
# -- returns index route --
@app.route("/")
def get_index():
    return "<p>Andreas web page</p>"
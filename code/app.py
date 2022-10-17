import os
from flask import Flask
from .data import get_account_data

app = Flask(__name__)

"""ENV varibales:
    AUTHOR
    DB_USERNAME
    DB_NAME
    DB_ADDRESS
    DB_PORT
    DB_PASSWORD
"""



@app.route("/")
def index():
    if(os.environ.get('AUTHOR')):
        return "Index Page!!! {}".format(os.environ.get('AUTHOR'))
    else:
        return "Index Page!!! No author"


@app.route('/hello/<string:user>')
def hello(user):
    return 'Hello, World {}'.format(user)


@app.route("/get_data/<string:username>")
def test(username):
    user_data = get_account_data(username)
    return "Username is {}".format(user_data)

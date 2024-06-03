from flask import render_template, Blueprint

home_route  = Blueprint('/', __name__)

@home_route.route('/')
def html():
    return render_template('index.html')

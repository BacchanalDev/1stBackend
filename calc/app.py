# Put your app in here.
from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

print('we are on math')

@app.route("/calc/add")
def add():
    '''It take 2 parameter and adds them
    >>> 4 + 5 = 9
    '''
    a=int(request.args.get("a"))
    b = int(request.args.get('b'))
    return 'Hey this is add page'

@app.route("/calc/sub")
def sub(a,b):
    '''It takes 2 parameters and subtracts them
    >>> 4 - 5 = -1
    '''
    a = int(request.args.get("a"))
    b = int(request.args.get('b'))
    return a-b

@app.route("/calc/mult")
def mult(a,b):
     '''It takes 2 parameters and multiplies them
    >>> 4 * 5 = 20
    '''
    a = int(request.args.get("a"))
    b = int(request.args.get('b'))
    return a * b

@app.route("/calc/div")
def div(a,b):
     '''It takes 2 parameters and divides them
    >>> 8/2 = 4
    '''
    a = int(request.args.get("a"))
    b = int(request.args.get('b'))
    return a/b
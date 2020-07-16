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
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = add(a,b)

    return str(result)

@app.route("/calc/sub")
def sub():
    '''It takes 2 parameters and subtracts them
    >>> 4 - 5 = -1
    '''
    a = int(request.args.get("a"))
    b = int(request.args.get('b'))
    result = sub(a,b)
    return str(result)

@app.route("/calc/mult")
def mult():
    '''It takes 2 parameters and multiplies them
    >>> 4 * 5 = 20
    '''
    # the args from query string do not go in the
    # params for the fx thats only variables
    a = int(request.args.get("a"))
    b = int(request.args.get('b'))
    result = mult(a,b)
    return str(result)

@app.route("/calc/div")
def div():
    '''It takes 2 parameters and divides them
    >>> 8/2 = 4
    '''
    a = int(request.args.get("a"))
    b = int(request.args.get('b'))
    result = div(a,b)
    return str(result)

# ----------------------------------------
#     part 2 would so that we have less routes


# operators = {
#         "add": add,
#         "sub": sub,
#         "mult": mult,
#         "div": div,
#         }

# @app.route("/calc/<oper>")
# def do_math(oper):
#     """Do math on a and b."""

#     a = int(request.args.get("a"))
#     b = int(request.args.get("b"))
#     result = operators[oper](a, b)

#     return str(result)
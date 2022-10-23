from flask import Flask, render_template, request, make_response, jsonify
from random import randint
import requests

app = Flask(__name__, instance_relative_config=True)

@app.route('/rand')
def rand():
    min = request.args.get('min', 0, type=int)
    max = request.args.get('max', 1000, type=int)
    if (min or min == 0) and (max or max == 0) and min <= max:
        return make_response(jsonify(randval=randint(min,max)), 200) # HTTP 200 OK
    else:
        return make_response('Invalid input\n', 400) # HTTP 400 BAD REQUEST

def create_app():
    return app

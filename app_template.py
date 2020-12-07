#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 20:49:53 2020

@author: bikash
"""

from subprocess import run, PIPE
from flask import Flask
from flask import request
from flask import render_template
from flask import make_response
from flask import jsonify
from flask_cors import CORS


{{config}}

app = Flask(__name__)
cors = CORS(app)

@app.route('/')
def homepage():
    '''render homepage'''
    return render_template("index.html", \
        text_input=text_input, numerical_input=numerical_input,\
            app_properties=app_properties)

@app.route('/app', methods=['POST'])
def myapp():
    try:

        args = ['./{{script_name}}',]
        for _, v in text_input.items():
            args.append('-{}'.format(v))
            args.append(request.form[v])

        for _, v in numerical_input.items():
            args.append('-{}'.format(v))
            args.append(request.form[v])

        res = run(args, stdout=PIPE, stderr=PIPE, check=False)
        response_dic = {
            "results": res.stdout.decode(),
            "errors": res.stderr.decode(),
        }
        return make_response(jsonify(response_dic), 200)
    except Exception as exp:
        return make_response(jsonify({"error":str(exp)}), 500)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5050', threaded=True, debug=False)

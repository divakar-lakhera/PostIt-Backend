from flask import Flask
from flask import request, jsonify
from flask_cors import CORS
from db import operations
app= Flask('PostIt-backend-service')


@app.route('/')
def index():
    return "LEZ GO"
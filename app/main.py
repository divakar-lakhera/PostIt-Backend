from flask import Flask
from flask import request, jsonify
from flask_cors import CORS

app = Flask("PostIt-backend-service")


@app.route("/")
def index():
    return "LEZ GO"

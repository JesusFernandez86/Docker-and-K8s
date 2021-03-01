from flask import Flask, jsonify
import pymongo
import os
from pymongo import MongoClient
import json_logging, logging, sys

app = Flask(__name__)

json_logging.init_flask(enable_json=True)
json_logging.init_request_instrument(app)
logger = logging.getLogger("cars_app")
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler(sys.stdout))

def get_db():
    client = MongoClient(host=os.environ['MONGODB_HOSTNAME'],
                         port=27017, 
                         username=os.environ['MONGODB_USERNAME'], 
                         password=os.environ['MONGODB_PASSWORD'],
                        authSource="admin")
    db = client[os.environ['MONGODB_DATABASE']]
    return db

@app.route('/')
def ping_server():
    return "Welcome to the second best website ever(v2)"

@app.route('/cars')
def get_stored_cars():
    db = get_db()
    _cars = db.car_tb.find()
    cars = [{"brand": car["brand"], "model": car["model"]} for car in _cars]
    return jsonify({"cars": cars})

@app.route('/health/live')
def health_live():
    return "Ok"

@app.route('/health/ready')
def health_ready():
    return "Ok"

if __name__=='__main__':
    app.run(host="0.0.0.0", port=5000)


"""
Created on Monday Dec 12 08:06:08 2020

@author: Vipul Bandwalkar
"""

# Necessary Library
import json
from bson import ObjectId
from bson.json_util import dumps
from pymongo import MongoClient  # Pymongo API of Mongodb
from flask import Flask, request, jsonify

app = Flask(__name__)

mongo = MongoClient("mongodb://localhost:27017/VipulDb")  # MongoDb Connection / Database Name


# Insertion Data In MongoDb
@app.route('/addData', methods=['POST'])
def addData():
    data = request.json
    name = data['name']
    img = data['img']
    summary = data['summary']
    if name and img and summary and request.method == 'POST':
        print(request.method)
        mongo.VipulDb.movies.insert({'name': name, 'img': img, 'summary': summary})
        response = jsonify('Data added successfully')
        response.status_code = 200

        return response
    else:
        return not_found()


# Get_Movies Json Data From Mongodb
@app.route('/Get_Movies')  # Get DB Data through End Point route
def users():
    users = mongo.VipulDb.movies.find()  # Database.Collection_Name
    response = dumps(users)
    return response


# Exception Handling for Errors
@app.errorhandler(404)
def not_found(error=None):
    message = {'status': 404, 'message': "Not Found" + request.url}

    response = jsonify(message)
    response.status_code = 404

    return response


"""Main Function,
    Port and host details set here"""
if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)

from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
from flask import jsonify


db_connect = create_engine("sqlite:///phonebook_API.db")
app = Flask(__name__)
api = Api(app)

class Customers(Resource):
    def get(self):
       conn =  db_connect.connect() # Connect to the database
       Query = conn.execute("Select * from customers") #performing a query and
       return {'Customers': [i[0] for i in query.cursor.fetchall()]} #Fetch first

class Tracks(Resource):
    def get(self):
        conn = db_connect.connect()
        query = conn.execute("select trackid, name, computer, unitprice from tracks")
        result = {'Data': [dict(zip(tuple(query.keys()),i)) for i in query.cursor]}
        return jsonify(result)


class Customer_Name(Resource):
    def get(self, customerid):
        conn = db_connect.connect()
        result = {'Data': [dict(zip(tuple (query.keys()),i)) for i in query.cursor]}
        return jsonify(result)

api.add_resource(Customers, '/customers')
api.add_resource(Tracks, '/tracks)')
api.add_resource(Customer_Name, '/customers/<customerid>')

if __name__ == "__main__":

    app.run(port='5002')

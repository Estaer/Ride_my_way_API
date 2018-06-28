from flask import Flask, request
from flask_restful import Resource, Api
from api.ridesview import RideRequest
from api.ridesview import RideOffer
from api.ridesview import Rides

APP = Flask(__name__)
API = Api(APP)
   

API.add_resource(Rides, '/api/v1/rides/')
API.add_resource(RideOffer, '/api/v1/rides/<string:offer_id>')
API.add_resource(RideRequest, '/api/v1/rides/<string:offer_id>/requests')

if __name__ == '__main__':
    APP.run(port=5000, debug=True)

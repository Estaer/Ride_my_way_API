from flask import Flask
from flask_restful import Resource, Api
from ride_details import All_Rides

APP = Flask(__name__)
API = Api(APP)

class Rides(Resource):
    """class for a Rides resource"""

    rides_object =  All_Rides()

    def get(self):

        """method to return all ride offers"""
        return {'message':'These are the available rides','rides':self.rides_object.get_rides()}, 200

class Rideoffer(Resource):
    """class for a Rideoffer resource"""
    rides_object =  All_Rides()

    def get(self, offer_id):
        """returns a ride offer for a specific offer id"""
        return {'message':'Here are the details for this ride','rides':self.rides_object.get_single_ride(offer_id)}, 200

API.add_resource(Rides, '/api/v1/rides/')
API.add_resource(Rideoffer, '/api/v1/rides/<string:offer_id>/')

if __name__ == '__main__':
    APP.run(port=5000, debug=True)

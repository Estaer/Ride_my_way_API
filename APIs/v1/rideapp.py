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




API.add_resource(Rides, '/api/v1/rides/')

if __name__ == '__main__':
    APP.run(port=5000, debug=True)

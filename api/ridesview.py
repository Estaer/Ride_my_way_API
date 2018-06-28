from flask_restful import Resource, request
from .models.ride_details import All_Rides

rides_object =  All_Rides()
class Rides(Resource):
    """class for a Rides resource"""
    def get(self):

        """method to return all ride offers"""
        return {'message':'These are the available rides','rides':rides_object.get_rides()}, 200
    
    def post(self):
        data = request.get_json() 
        new_ride = rides_object.post_ride(data['rideId'], data['driver_id'], data['meetingpoint'], data['departure'], data['destination'], data['slots'])
        return {'message': 'Offer created'}, 201

class RideOffer(Resource):
    """class for a Rideoffer resource"""

    def get(self, rideId):
        """returns a ride offer for a specific offer id"""
        return rides_object.get_single_ride(rideId), 200


class RideRequest(Resource):
    
    def post(self, rideId):
        data = request.get_json() 
        new_request = rides_object.make_request(rideId, data['request_id'], 'PENDING')
        return {'message': 'Request Made'}, 201
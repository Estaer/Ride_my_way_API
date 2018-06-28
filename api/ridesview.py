from flask_restful import Resource
from .models.ride_details import All_Rides

rides_object =  All_Rides()
class Rides(Resource):
    """class for a Rides resource"""

    

    def get(self):

        """method to return all ride offers"""
        return {'message':'These are the available rides','rides':rides_object.get_rides()}, 200
    
    def post(self):
        data = request.get_json() 
        new_ride = rides_object.post_ride(data['offer_id'], data['driver_id'], data['meetingpoint'], data['departure'], data['destination'], data['slots'])
        return {'message': 'Offer created'}, 201

class RideOffer(Resource):
    """class for a Rideoffer resource"""

    def get(self, offer_id):
        """returns a ride offer for a specific offer id"""
        return {'message':'Here are the details for this ride','rides':rides_object.get_single_ride(offer_id)}, 200


class RideRequest(Resource):
    
    def post(self, offer_id):
        data = request.get_json() 
        new_request = rides_object.make_request(offer_id, data['request_id'], 'PENDING')
        return {'message': 'Request Made'}, 201
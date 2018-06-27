class Ride: 

    def __init__(self, offer_id, driver_id, meetingpoint, departure, destination, slots):
        self.offer_id = offer_id
        self.driver_id = driver_id
        self.meetingpoint = meetingpoint
        self.departure = departure
        self.destination = destination
        self.slots = slots


class All_Rides:

    # lists of all rides
    rides = []

    def get_rides(self):
        return [ride.__dict__ for ride in self.rides] 

    def get_single_ride(self, offer_id):

        for ride in self.rides:
            if ride.offer_id == offer_id:
                return ride.__dict__
            else:
                return {'message':'Ride doesnot exist'}, 201



All_Rides.rides.append(Ride('R01', 'D01', 'Buziga', '12/06/18 9:00am', 'Nakawa', 5))
All_Rides.rides.append(Ride('R02', 'D02', 'Makerere', '14/06/18 9:00am', 'Kyanja', 3))
All_Rides.rides.append(Ride('R03', 'D03', 'Kololo', '15/06/18 9:00am', 'Kisaasi', 1))
All_Rides.rides.append(Ride('R04', 'D04', 'Kiwatule', '16/06/18 9:00am', 'Bukoto', 4))

    
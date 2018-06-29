import unittest
import json
import sys,os
sys.path.append(os.path.pardir)
from run import APP

class TestClass(unittest.TestCase):
    def setUp(self):

        self.myapp = APP.test_client()
        

    def test_Get_endpoints(self):
        # test for a valid status code
        response = self.myapp.get('/api/v1/rides')
        self.assertEqual(response.status_code, 200)
        # test for datatypes 
        self.assertIsInstance(response.json["rides"], list)

        data = json.loads(response.data.decode())
        self.assertTrue(data['message'] == 'These are the available rides')

    def test_post_rideoffer(self):
        """method to test ride offers"""
        # valid status code
        response = self.myapp.post('/api/v1/rides',
        data = json.dumps(dict(
            rideId ='R07', 
            driver_id = 'DO7',
            meetingpoint = 'buziga',
            departure = '16/06/18 9:00am',
            destination = 'ggg',
            slots = 2)),
            content_type = 'application/json')

        self.assertEqual(response.status_code, 201)

        data = json.loads(response.data.decode())
        self.assertTrue(data['message'] == 'Ride Offer created')

    
    def test_Get_singleride(self):
        # test for a valid status code
        response = self.myapp.get('/api/v1/rides/R07')
        self.assertEqual(response.status_code, 200)
    
    def test_make_request(self):
        # test for a valid status code
        
        response = self.myapp.post('/api/v1/rides/R07/requests', 
        data = json.dumps(dict(
            request_id = 'rw01')),
            content_type = 'application/json')
        self.assertEqual(response.status_code, 201)

        data = json.loads(response.data.decode())
        self.assertTrue(data['message'] == 'Request Made')

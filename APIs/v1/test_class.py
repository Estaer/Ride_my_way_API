import unittest
import json
from rideapp import APP

class TestClass(unittest.TestCase):
    def setUp(self):

        self.myapp = APP.test_client()
        

    def test_Get_endpoint(self):
        # test for a valid status code
        response = self.myapp.get('/api/v1/rides/')
        self.assertEqual(response.status_code, 200)
        # test for datatypes 
        self.assertIsInstance(response.json['rides'], list)
        self.assertIsInstance(response.json['rides'][0], dict)
        self.assertIsInstance(response.json['rides'][1], dict)
        self.assertIsInstance(response.json['rides'][2], dict)
        self.assertIsInstance(response.json['rides'][3], dict)
        # test length of list
        self.assertTrue(len(response.json['rides']) >= 4)

        data = json.loads(response.data.decode())
        self.assertTrue(data['message'] == 'These are the available rides')
    
    def test_Get_singleride_endpoint(self):
        # test for a valid status code
        response = self.myapp.get('/api/v1/rides/R01')
        self.assertEqual(response.status_code, 200)
        # test for datatypes 
        self.assertIsInstance(response.json['rides'], dict)

        data = json.loads(response.data.decode())
        self.assertEqual(data['message'], 'Here are the details for this ride')
        
        
        
        


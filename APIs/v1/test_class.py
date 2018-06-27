import unittest
import json
from rideapp import APP

class TestClass(unittest.TestCase):
    def setUp(self):

        self.myapp = APP.test_client()
        

    def test_Get_endpoints(self):
        # test for a valid status code
        response = self.myapp.get('/api/v1/rides/')
        self.assertEqual(response.status_code, 200)
        # test for datatypes 
        self.assertIsInstance(response.json["rides"], list)
        self.assertIsInstance(response.json["rides"][0], dict)
        self.assertIsInstance(response.json["rides"][1], dict)
        self.assertIsInstance(response.json["rides"][2], dict)
        self.assertIsInstance(response.json["rides"][3], dict)
        # test length of list
        self.assertTrue(len(response.json["rides"]) >= 4)


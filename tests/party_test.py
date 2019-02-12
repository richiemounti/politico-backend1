import os
import sys
import json
import unittest
from instance.config import configs
from politicer import create_app


sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class TestParty(unittest.TestCase):
    """docstring for TestParty"""

    def setUp(self):
        self.app = create_app(test_config="testing")  
        self.client2= self.app.test_client()

        self.data = {
            "name": "Party A",
            "hqAddress": "50200 Nairobi",
            "logoUrl": "sojri.png"
        }
        self.data1 = {
            "name": "Party B",
            "hqAddress": "50200 Nairobi",
            "logoUrl": "sojri.png"
        }
        self.data2 = {
            "name": "Party C",
            "hqAddress": "50200 Nairobi"
        }
        self.data3 = {
            "name": "co",
            "logoUrl": "sojri.png",
        }
        self.office = {
            "name": "Johny English",
            "type": "Legislative",
        }
        self.office1 = {
            "name": "Joe Muchiri",
            "type": "Federal",
        }
        self.office2 = {
            "name": "Babu Owino",
            "type": "Federal",
        }
    
    ''' @app.route '''
    def test_default_route(self):
        res = self.client2.get('/')
        dataCheck = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertTrue('status' in dataCheck)
    
    ''' error handlers '''
    def test_page_not_found(self):
        res = self.client2.get('/page')
        dataCheck = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.check_reply(dataCheck, 404, error=True)

    def test_method_not_allowed(self):
        res = self.client2.post('/')
        dataCheck = json.loads(res.data)
        self.assertEqual(res.status_code, 405)
        self.check_reply(dataCheck, 404, error=True)

    def check_reply(self, dataCheck, status, error=False):
        self.assertTrue('status' in dataCheck)
        if not error:
            self.assertTrue('data' in dataCheck)
        else:
            self.assertTrue('error' in dataCheck)
    
    

if __name__ == '__main__':
    unittest.main()

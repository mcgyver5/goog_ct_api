import unittest
import json
import os
import ctlogs
TESTDATA_FILENAME = os.path.join(os.path.dirname(__file__), 'crt.sh.json')

class TestCTLogs(unittest.TestCase):
    
    def setUp(self):
        self.testfile = open(TESTDATA_FILENAME)
        self.testdata = self.testfile.read()

    def tearDown(self):
        self.testfile.close()

    
    def test_json_read(self):
        my_domain_list = ctlogs.get_domains_from_json(self.testdata)
        first_domain = my_domain_list[0]
        expected = "dli.mn.gov"
        self.assertEqual(expected,first_domain)

    def test_calling_url(self):
        my_domain_list = ctlogs.get_domains_from_api("dhs.state.mn.us")
        expected = "qa.childsupport.dhs.state.mn.us"
        domain_in_list = expected in my_domain_list
        self.assertTrue(domain_in_list)
if __name__ == '__main__':
    unittest.main()

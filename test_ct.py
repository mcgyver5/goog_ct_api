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


    def test_UnitTest(self):
        expected = 12
        actual = 3 * 4
        self.assertEqual(expected, actual)
    
    
    def test_json_read(self):
        my_domain_list = ctlogs.get_domains_from_json(self.testdata)
        print(my_domain_list)
        first_domain = my_domain_list[0]
        expected = "dli.mn.gov"
        
        self.assertEqual(expected,first_domain)

    def test_calling_url(self):
        my_domain_list = ctlogs.get_domains_from_api("dhs.state.mn.us")
        print(len(my_domain_list))
        expected = "qa.childsupport.dhs.state.mn.us"
        for x in my_domain_list:
            print(x)
            if x == expected:
                print("aha!!!!")

        domain_in_list = expected in my_domain_list
        print(domain_in_list)
        self.assertTrue(domain_in_list)
if __name__ == '__main__':
    unittest.main()

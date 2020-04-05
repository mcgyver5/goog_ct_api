import unittest
import ctlogs

class TestCTLogs(unittest.TestCase):

    def test_UnitTest(self):
        expected = 12
        actual = 3 * 4
        self.assertEqual(expected, actual)
    
    def test_API_request(self):
        expected = 200
        actual = ctlogs.requestLogs()
if __name__ == '__main__':
    unittest.main()

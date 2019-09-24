import unittest

import yourapplication


class YourapplicationTestCase(unittest.TestCase):

    def setUp(self):
        self.app = yourapplication.app.test_client()

    def test_index(self):
        rv = self.app.get('/')
        self.assertIn('Welcome to test-cookie-cutter', rv.data.decode())


if __name__ == '__main__':
    unittest.main()

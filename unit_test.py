import unittest

from app import app

class TestPlus(unittest.TestCase):
    def test_true_when_x_is_17(self):
        response,statuscode = app.is_prime(17)
        self.assertEqual(statuscode, 200)
        self.assertEqual(response.json, {"result": True})
    def test_false_when_x_is_36(self):
        response,statuscode = app.is_prime(36)
        self.assertEqual(statuscode, 200)
        self.assertEqual(response.json, {"result": False})
    def test_true_when_x_is_13219(self):
        response,statuscode = app.is_prime(13219)
        self.assertEqual(statuscode, 200)
        self.assertEqual(response.json, {"result": True})


if __name__ == '__main__':
    unittest.main()
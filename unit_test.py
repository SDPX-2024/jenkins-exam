import unittest

from app import app

class TestPlus(unittest.TestCase):
    # def test_true_when_x_is_17(self):
    #     response,statuscode = app.is_prime(17)
    #     self.assertEqual(statuscode, 200)
    #     self.assertEqual(response.json, {"result": True})
    # def test_false_when_x_is_36(self):
    #     response,statuscode = app.is_prime(36)
    #     self.assertEqual(statuscode, 200)
    #     self.assertEqual(response.json, {"result": False})
    # def test_true_when_x_is_13219(self):
    #     response,statuscode = app.is_prime(13219)
    #     self.assertEqual(statuscode, 200)
    #     self.assertEqual(response.json, {"result": True})
    def test_x_is_1(self):
        response,statuscode = app.cir_area(1)
        self.assertEqual(statuscode, 200)
        self.assertEqual(response.json, {"result": 3.14})
    def test_x_is_neg10(self):
        response,statuscode = app.cir_area(-10)
        self.assertEqual(statuscode, 200)
        self.assertEqual(response.json, {"result": 0.00})
    def test_x_is_1dot5(self):
        response,statuscode = app.cir_area(1.5)
        self.assertEqual(statuscode, 200)
        self.assertEqual(response.json, {"result": 7.07})

if __name__ == '__main__':
    unittest.main()

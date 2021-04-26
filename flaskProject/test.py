# This code is made by Eric Tiancheng Gu (c) 2021

try:
    from app import app
    import unittest
    from flask import request

except Exception as e:
    print("Some modules are missing, please check".format(e))


class MyTestCase(unittest.TestCase):
    """
    def test_response(self):
        with app.test_request_context():
            c = app.test_client()
            response = c.get('/checkips')

        return response
    """
    # ensure flask app was set up nicely
    def test_index(self):
        tester = app.test_client(self)
        response = tester.post('/checkips')
        self.assertEqual(response.status_code, 200)

    # test data, specifically if it works for this ip
    def test_checkips(self):
        tester = app.test_client(self)
        # replace data with something that is found in the url
        response = tester.post('/checkips', data = '{"ips":["62.210.105.116"]}', content_type = "application/json")
        self.assertIn(b'1', response.data)


if __name__ == '__main__':
    unittest.main()

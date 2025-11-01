from wmata_api import app
import json
import unittest


class WMATATest(unittest.TestCase):
    # Ensure both endpoints return a 200 HTTP code
    def test_http_success(self):
        escalator_response = (app.test_client().
                              get('/incidents/escalators').status_code)
        # Assert that the response code of 'incidents/escalators'
        # returns a 200 code
        self.assertEqual(escalator_response, 200)

        elevator_response = (app.test_client().
                             get('/incidents/elevators').status_code)
        # assert that the response code of 'incidents/elevators
        # returns a 200 code
        self.assertEqual(elevator_response, 200)

#######################################################################

    # Ensure all returned incidents have the 4 required fields.
    def test_required_fields(self):
        required_fields = ["StationCode", "StationName", "UnitType",
                           "UnitName"]

        # Parse out escalator incidents.
        response_escalators = (app.test_client().
                               get('/incidents/escalators'))
        json_response_escalators = json.loads(response_escalators.
                                              data.decode())
        # Parse out elevator incidents.
        response_elevators = (app.test_client().
                              get('/incidents/elevators'))
        json_response_elevators = (json.loads
                                   (response_elevators.data.decode()))

        # For each incident in the JSON response assert that each of
        # the required fields are present in the response.
        #
        # Use a nested for loop to check if each field is in each
        # dictionary. Do this for both elevator and escalator
        # incidents.
        for item in json_response_escalators:
            for field in required_fields:
                self.assertIn(field, item)

        for item in json_response_elevators:
            for field in required_fields:
                self.assertIn(field, item)

#######################################################################

    # Ensure all entries returned by the escalators endpoint have a
    # UnitType of "ESCALATOR"
    def test_escalators(self):
        response = app.test_client().get('/incidents/escalators')
        json_response = json.loads(response.data.decode())

        # For each incident in the JSON response, assert that the
        # 'UnitType' is "ESCALATOR"
        for item in json_response:
            self.assertEqual(item["UnitType"], "ESCALATOR")

#######################################################################

    # Ensure all entries returned by the elevators endpoint have a
    # UnitType of "ELEVATOR"
    def test_elevators(self):
        response = app.test_client().get('/incidents/elevators')
        json_response = json.loads(response.data.decode())

        # For each incident in the JSON response, assert that the
        # 'UnitType' is "ELEVATOR"
        for item in json_response:
            self.assertEqual(item["UnitType"], "ELEVATOR")

#######################################################################

if __name__ == "__main__":
    unittest.main()

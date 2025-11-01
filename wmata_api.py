import json
import requests
from flask import Flask

# API endpoint URL's and access keys
WMATA_API_KEY = "cff72774ee904e95b645b049dc5a18c4"
INCIDENTS_URL = "https://api.wmata.com/Incidents.svc/json/ElevatorIncidents"
headers = {"api_key": WMATA_API_KEY, 'Accept': '*/*'}

########################################################################

app = Flask(__name__)

# Get incidents by machine type (elevators/escalators)
# Field is called "unit_type" in WMATA API response
@app.route("/incidents/<unit_type>", methods=["GET"])


# This function will return a json string.
def get_incidents(unit_type) -> str:
    # create an empty list called 'incidents'
    incidents = []

    # Sse 'requests' to do a GET request to the WMATA Incidents API
    # Retrieve the JSON from the response
    incident_request = requests.get(INCIDENTS_URL, headers=headers)
    incident_request_json = incident_request.json()
    incident_dictionaries = (incident_request_json.get
                             ("ElevatorIncidents"))

    # Iterate through the JSON response and retrieve all incidents
    # matching 'unit_type'. As per the assignment instructions,
    # 'unit_type' will be elevators and escalators.
    #
    # For each incident, create a dictionary containing the 4 fields
    # from the Module 7 API definition
    #
    # The 4 fields are: StationCode, StationName, UnitType, UnitName
    # Add each incident dictionary object to the 'incidents' list
    # Return the list of incident dictionaries using json.dumps()
    for item in incident_dictionaries:
        if unit_type == "elevators" and item["UnitType"] == "ELEVATOR":
            incidents.append({"StationCode" : item.get("StationCode"),
                              "StationName" : item.get("StationName"),
                              "UnitType" : item.get("UnitType"),
                              "UnitName" : item.get("UnitName")})

        elif (unit_type == "escalators" and item["UnitType"] ==
              "ESCALATOR"):
            incidents.append({"StationCode" : item.get("StationCode"),
                              "StationName" : item.get("StationName"),
                              "UnitType" : item.get("UnitType"),
                              "UnitName" : item.get("UnitName")})
        # Skip all 'unit_type" that are not escaltors or elevators.
        else:
            continue

    return json.dumps(incidents)

if __name__ == '__main__':
    app.run(debug=True)

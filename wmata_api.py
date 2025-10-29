import json
import requests
from flask import Flask

# API endpoint URL's and access keys
WMATA_API_KEY = "cff72774ee904e95b645b049dc5a18c4"
INCIDENTS_URL = "https://api.wmata.com/Incidents.svc/json/ElevatorIncidents"
headers = {"api_key": WMATA_API_KEY, 'Accept': '*/*'}

################################################################################

app = Flask(__name__)

# get incidents by machine type (elevators/escalators)
# field is called "unit_type" in WMATA API response
@app.route("/incidents/<unit_type>", methods=["GET"])
def get_incidents(unit_type) -> str:
    # create an empty list called 'incidents'
    incidents = []

    # use 'requests' to do a GET request to the WMATA Incidents API
    # retrieve the JSON from the response
    incident_request = requests.get(INCIDENTS_URL, headers=headers)
    incident_request_json = incident_request.json()
    incident_dictionaries = incident_request_json.get("ElevatorIncidents")


    # iterate through the JSON response and retrieve all incidents matching 'unit_type'
    # for each incident, create a dictionary containing the 4 fields from the Module 7 API definition
    #   -StationCode, StationName, UnitType, UnitName
    # add each incident dictionary object to the 'incidents' list
    # return the list of incident dictionaries using json.dumps()

    for item in incident_dictionaries:
        if unit_type == "elevators" and item["UnitType"] == "ELEVATOR":
            incidents.append({"StationCode" : item.get("StationCode"), "StationName" : item.get("StationName"), "UnitType" : item.get("UnitType"), "UnitName" : item.get("UnitName")})

        elif unit_type == "escalators" and item["UnitType"] == "ESCALATOR":
            incidents.append({"StationCode" : item.get("StationCode"), "StationName" : item.get("StationName"), "UnitType" : item.get("UnitType"), "UnitName" : item.get("UnitName")})

        else:
            continue

    return json.dumps(incidents)

if __name__ == '__main__':
    app.run(debug=True)

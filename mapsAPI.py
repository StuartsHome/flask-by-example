
# Ability to dynamically query Google Maps through the Google Directions API.
# As an example, this request calculates the route from Chicage, IL to Los Angeles, CA via
# two waypoints in Joplin, MO and Oklahoma City, OK.


import requests

url = "http://maps.googleapis.com/maps/api/directions/json"

params = dict(
    origin='Chicago,IL',
    destination='Los+Angeles,CA',
    waypoints='Joplin,MO|Oklahoma+City,OK',
    sensor='false'

)

resp = requests.get(url=url, json=params)
#params=params)
data = resp.json() # check the JSON Response Content documentation

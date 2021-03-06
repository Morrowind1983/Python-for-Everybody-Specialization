# Exercise 1: Change either the www.py4e.com/code3/geojson.py or
# www.py4e.com/code3/geoxml.py to print out the two-character country code from
# the retrieved data. Add error checking so your program does not traceback if
# the country code is not there. Once you have it working, search for "Atlantic
# Ocean" and make sure it can handle locations that are not in any country.

import urllib.request, urllib.parse, urllib.error
import json

# Note that Google is increasingly requiring keys
# for this API
serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'

while True:
    address = input('Enter location: ')
    if len(address) < 1:
        break

    url = serviceurl + urllib.parse.urlencode({'address': address})

    print('Retrieving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    print(json.dumps(js, indent=4))

    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]
    print('lat', lat, 'lng', lng)
    location = js['results'][0]['formatted_address']
    print(location)
    
    address_components = js["results"][0]['address_components']
    country_code = None
    for address in address_components:
        types = address['types'][0]
        if types == "country":
            country_code = address['short_name']
    if country_code is None:
        print("No country code")
        continue
    print("country code:", country_code)

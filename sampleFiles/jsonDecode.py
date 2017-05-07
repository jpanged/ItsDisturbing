import json
#import requests
import urllib.request
json_bytes = urllib.request.urlopen(
    "http://fs.fire-light.us/siliconHacks/jsonDataSample.txt").read()

input_data = json_bytes.decode("utf-8")
# This converts from JSON to a python dict
parsed_input = json.loads(input_data)
# This parses the JSON datas
currentTemperature = parsed_input['currently']
sunriseSunest = parsed_input['daily']
temperature = (currentTemperature['temperature'])
sunsetTime = (sunriseSunest['data'][0]['sunsetTime'])
sunriseTime = (sunriseSunest['data'][0]['sunriseTime'])
print("OUTPUT")
print(parsed_input)
print(temperature)
print(sunsetTime)
print(sunriseTime)

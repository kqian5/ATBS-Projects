#! python3
# quickWeather.py - Prints a weather for the location from the command line

import json, sys, requests

if len(sys.argv) < 2:
    print("Usage: python quickWeather.py location")
    sys.exit()

location = " ".join(sys.argv[1:])

url = "http://api.openweathermap.org/data/2.5/weather?q=%s&appid=886705b4c1182eb1c69f28eb8c520e20" % location
response = requests.get(url)
response.raise_for_status()

json_formatted = json.loads(response.text)

for key in json_formatted["main"]:
    print(str(key) + " is " + str(json_formatted["main"][key]) + "\n")
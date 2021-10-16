#open openweathermap.org> navigate to api
import requests

#api_key = ""
city =  "Orlando"
#api call
#url = "http://"

#requests = requests.get(url)
json = requests.json
print(json)

description = json.get("weather")[0].get("description")
print(description)

#temp_main = json.get(main).get("temp_min")
#print(temp_main)

#temp_max = json.get(main).get("temp_max")
#print(temp_max)
#go to jsonformatter.curiousconcept.com

#
# {
#    "name":"John",
#    "age":30,
#    "car":null
# }


#open openweathermap.org> navigate to api
import requests

def get_weather_desc_and_temp():
    #api_key = ""
    city =  "Orlando"
    #api call
    #url = "http://"

    #requests = requests.get(url)
    json = requests.json
    print(json)

    description = json.get("weather")[0].get("description")
    print(description)

    #temp_min = json.get(main).get("temp_min")
    #print(temp_min)

    #temp_max = json.get(main).get("temp_max")
    #print(temp_max)

    return {'description':description,
    #        'temp_min' : temp_min,
    #       'temp_max' : temp_max,
    }
#getting the function values in dict

def main():
    weather_dict = get_weather_desc_and_temp()
    print(" Today's forecast description " , weather_dict.get('description'))
    #print(" Today's forecast description " , weather_dict.get('temp_min'))
    #print(" Today's forecast description " , weather_dict.get('temp_max'))
main()








    #go to jsonformatter.curiousconcept.com

#
# {
#    "name":"John",
#    "age":30,
#    "car":null
# }


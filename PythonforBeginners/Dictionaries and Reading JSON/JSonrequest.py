#note requests.readthedocs.io/en/master
#python -m pip install requests
#open-notify.org

import requests

response = requests.get('http://api.open-notify.org/astros.json') #get json from this link
json = response.json() #getting json
print(json)

for person in json['people']: 
    print(person['name'])
# 2. The Web-service being called from someplace else (Testing Code)

import requests

url = 'http://localhost:9696/predict'
# url = 'http://127.0.0.1:9696/predict'

client = {
    "lead_source": "organic_search",
    "number_of_courses_viewed": 4,
    "annual_income": 80304.0
}

response = requests.post(url, json=client).json()

print(response)
if response['subscribe'] == True:
   print('client is likely to get a subscription')
else:
   print('client is NOT likely to get a subscription')
import requests
import os
import json

api_key = os.getenv('CLIMACELL_API_KEY')
api_url = 'https://data.climacell.co/v4/timelines'
chs_coords= '37.7765,79.9311'
queryParams = {
  'location' : chs_coords,
  'fields' : ['epaHealthConcern', 'epaPrimaryPollutant'],
  'units' : 'imperial',
  'timesteps' : '1h'
}

# items = [1, 2, 3, 4, 5]
# squared = list(map(lambda x: x**2, items))

r_headers = { 'apiKey': api_key }
def get_airQuality(): 
    r = requests.get(
      api_url, 
      params=queryParams,
      headers=r_headers
    )
    response_data = r.json()

    air_quality_list = response_data['data']['timelines'] 
    value = list(map(lambda item : 
      { 
        'star_time': item.get('startTime'),
        'healthConcern' : item.get('values', {}).get('epaHealthConcern') ,
        'primaryPollutant': item.get('values', {}).get('epaPrimaryPollutant')
      },
    air_quality_list))
    print(f"WORKING? {value}")
    return value


get_airQuality()
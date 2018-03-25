import pyowm
import json

api = pyowm.OWM('0d24b5f810c4a57bb781502ca90d6d1a')

latitude = float('41.9973')
longtitude = float('21.4280')

area = api.weather_around_coords(latitude, longtitude)
locations = []
for place in area:
    locations.append(json.loads(place.to_JSON()))

weather_conds = [w['Weather']['status'] for w in locations]
print weather_conds
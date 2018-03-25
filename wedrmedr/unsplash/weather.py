import pyowm
import json


def get_conditions():
    '''
Returns:
    Set of (unique) weather conditions in area around coordinates.
Example:
    clouds, haze, heavy snow
    '''
    api = pyowm.OWM('0d24b5f810c4a57bb781502ca90d6d1a')

    latitude = float('41.9973')
    longtitude = float('21.4280')

    area = api.weather_around_coords(latitude, longtitude)

    locations = []
    for place in area:
        locations.append(json.loads(place.to_JSON()))

    weather_conds = set([w['Weather']['status'] for w in locations])
    return weather_conds if any(weather_conds) else 'thunderstorm'

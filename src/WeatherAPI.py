import requests
import json
from src.config import API_KEY

class WeatherAPI:
    def consultaAPI (self,city_name,country_code):
        
        params = {
            'q':[city_name,country_code],
            'appid':{API_KEY}
                }

        url = 'https://api.openweathermap.org/geo/1.0/direct?'
        response = requests.get(url, params = params)
        return json.loads(response.text)

    def obter_coord(self, response):
        print(response)
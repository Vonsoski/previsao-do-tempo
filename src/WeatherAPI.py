import requests
import json
from src.config import API_KEY

class WeatherAPI:
    def consulta_city (self,city_name,state_code,country_code):
        
        params = {
            'q': f"{city_name},{state_code},{country_code}",
            'appid': API_KEY,
            'lang': 'pt'
        }
        url = 'https://api.openweathermap.org/geo/1.0/direct?'
        response = requests.get(url, params = params)
        return json.loads(response.text)
    
    def obter_coord(self, response):
        lat = response[0]['lat']
        lon = response[0]['lon']
        return lat, lon
    
    def info_tempo (self, lat, lon):
        params = {
            'lat': lat,
            'lon': lon,
            'appid': API_KEY,
            'lang': 'pt'
        }
        url = 'https://api.openweathermap.org/data/2.5/weather?'
        self.response = requests.get(url, params = params)
        return json.loads(self.response.text)
    
    def consulta_temperatura (self, response):
        temperatura = response['main']['temp']
        descricao = response['weather'][0]['description']
        pais = response['sys']['country']
        cidade = response['name']
        print(cidade)
        weather = round(temperatura - 273.15)
        return descricao, weather, pais, cidade
    
import modulos as consultas
#dados cidade, no country_code, precisa estar de acordo com a ISO 3166-2BR
city_name = 'Sergipe'
country_code = 'BR-SE'

#Chama class
consulta_api = consultas.WeatherAPI()
consulta = consulta_api.consultaAPI(city_name,country_code)
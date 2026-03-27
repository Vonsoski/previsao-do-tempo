import modulos as consultas
#dados cidade
city_name = 'Sergipe'
country_code = 'BR-SE'

#Chama class
consulta_api = consultas.WeatherAPI()
consulta = consulta_api.consultaAPI(city_name,country_code)
import modulos as consultas
#dados cidade, no country_code, precisa estar de acordo com a ISO 3166-2BR
city_name = 'Aracaju'
state_code = 'SE'
country_code = 'BR'

#Cria o objeto
consulta_api = consultas.WeatherAPI()
#Chama classe para consultar e obter o json
consulta = consulta_api.consulta_city(city_name, state_code, country_code)

#Obtem as coordernadas e os valores
lat, lon = consulta_api.obter_coord(consulta)

#Envia latitude e longitude para obter os dados como temperatura e afins
consulta_city = consulta_api.info_tempo(lat, lon)

#Consulta a temperatura
descricao, graus, pais, cidade = consulta_api.consulta_temperatura(consulta_city)

print(graus)
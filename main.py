import logging
import modulos as consultas

logging.basicConfig(filename='log/app.txt', level=logging.ERROR, format=" %(asctime)s - %(levelname)s - %(message)s - linha %(lineno)d")
#dados cidade, no country_code, precisa estar de acordo com a ISO 3166-2BR
city_name = 'Araçatuba'
state_code = 'SP'
country_code = 'BR'

try:
    #Cria o objeto
    consulta_api = consultas.WeatherAPI()
    #Chama classe para consultar e obter o json
    response, retorno_text = consulta_api.consulta_city(city_name, state_code, country_code)

    if response == 200:
        #Obtem as coordernadas e os valores
        lat, lon = consulta_api.obter_coord(retorno_text)

        #Envia latitude e longitude para obter os dados como temperatura e afins
        consulta_city = consulta_api.info_tempo(lat, lon)

        #Consulta a temperatura
        descricao, graus, pais, cidade = consulta_api.consulta_temperatura(consulta_city)

        print(f"A cidade {cidade}-{pais}, esta com o {descricao}, atualmente faz {graus} graus.")
    else:
        logging.error(f"Ocorreu um erro na consulta da api {response}")
except:
    logging.error(f"Ocorreu um erro")
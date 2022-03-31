import json
import configparser
import requests

from utils.resources import *
from utils.configurations import *

url = getConfig()['API']['endpoint'] + ApiResources.fight_pokemon
first_gen = '151'
fight_list_pokemon_response = requests.get(url).json()
fight_list_pokemon = fight_list_pokemon_response['pokemon']

pokemon_fight_weights = [0,50000]

for pokemon in fight_list_pokemon:
    temp_url = pokemon['pokemon']['url']
    temp_id = temp_url.split("/")[-2:-1][0]
    if(temp_id <= first_gen):
        pokemon_info_response = requests.get(temp_url).json()
        if (pokemon_info_response['weight'] > pokemon_fight_weights[0]):
            pokemon_fight_weights[0] = pokemon_info_response['weight']
        elif (pokemon_info_response['weight'] < pokemon_fight_weights[1]):
            pokemon_fight_weights[1] = pokemon_info_response['weight']
print(pokemon_fight_weights)

import json
import configparser
import requests

from utils.resources import *
from utils.configurations import *

url = getConfig()['API']['endpoint'] + ApiResources.list_pokemon
list_pokemon_response = requests.get(url).json()
total_items = list_pokemon_response['count']

list_pokemon_response = requests.get(url,params={'limit':total_items}).json()
list_pokemon = list_pokemon_response['results']
count = 0

for pokemon in list_pokemon:
    print(pokemon)
    if ("at" in pokemon['name']) and (pokemon['name'].count("a") > 1):
        count += 1

print(count)

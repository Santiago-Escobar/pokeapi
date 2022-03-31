import json
import configparser
import requests

from utils.resources import *
from utils.configurations import *

url = getConfig()['API']['endpoint'] + ApiResources.raichu_pokemon
get_species_url_from_raichu = requests.get(url).json()['species']['url']

get_egg_groups_for_species = requests.get(get_species_url_from_raichu).json()['egg_groups']
list_of_pokemons = set()
for group in get_egg_groups_for_species:
    pokemon_species_response = requests.get(group['url']).json()['pokemon_species']
    mapped_list = map(lambda obj: obj['name'],pokemon_species_response)
    temp_set_pokemons = set(mapped_list)
    list_of_pokemons = list_of_pokemons.union(temp_set_pokemons)

print(len(list_of_pokemons))






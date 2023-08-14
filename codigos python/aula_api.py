import requests

pokemon_name = 'mewtwo'

response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}')
data = response.json()

print(f"Nome: /{data['name'].capitalize()}")
print(f"Altura: {data['height']/10} metros")
print(f"Peso: {data['weight']/10} kg")
import requests
from bs4 import BeautifulSoup


# Define the URL of the page
URL = 'https://pokemondb.net/pokedex/all'

# Fetch the HTML content using requests
response = requests.get(URL)
response.raise_for_status()  # Raise an exception for HTTP errors
# with open("pokemon_page.html", "w", encoding='utf-8') as file:
#     file.write(response.text)
#     file.close()

# Parse the content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find the table containing the Pokémon data
pokemon_table = soup.find('table', id='pokedex')

# Fetch the Pokémon rows
pokemon_rows = pokemon_table.tbody.find_all('tr')

# Create a list to store Pokémon data
pokemons = []

# Loop through each row to extract data
for row in pokemon_rows:
    columns = row.find_all('td')
    
    # Extracting data from the columns
    number = columns[0].text.strip()
    name = columns[1].text.strip()
    type_ = columns[2].text.strip()
    total = columns[3].text.strip()
    hp = columns[4].text.strip()
    attack = columns[5].text.strip()
    defense = columns[6].text.strip()
    sp_atk = columns[7].text.strip()
    sp_def = columns[8].text.strip()
    speed = columns[9].text.strip()
    
    pokemon_data = {
        'Number': number,
        'Name': name,
        'Type': type_,
        'Total': total,
        'HP': hp,
        'Attack': attack,
        'Defense': defense,
        'Sp. Atk': sp_atk,
        'Sp. Def': sp_def,
        'Speed': speed
    }
    
    pokemons.append(pokemon_data)

# Print the first 5 Pokémon data for testing
for pokemon in pokemons[:5]:
    print(pokemon)

# Save the data in a CSV file
# import csv

# with open('pokemons.csv', 'w', encoding='utf-8') as file:
#     writer = csv.DictWriter(file, fieldnames=pokemon_data.keys())
#     writer.writeheader()
#     writer.writerows(pokemons)
#     file.close()
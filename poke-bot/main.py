import discord
from discord.ext import commands
import requests
from bs4 import BeautifulSoup

# DISCORD SETUP
DISCORD_TOKEN = ""
PREFIX = "!"

bot = commands.Bot(command_prefix=PREFIX, intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f"{bot.user.name} is connected to the server.")

@bot.command()
async def ping(ctx):
    await ctx.send(f"Pong! {round(bot.latency * 1000)}ms")

# POKEMON SCRAPER FUNCTIONS
def fetch_pokemon_data():
    try:
        URL = 'https://pokemondb.net/pokedex/all'
        response = requests.get(URL)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        pokemon_table = soup.find('table', id='pokedex')
        pokemon_rows = pokemon_table.tbody.find_all('tr')
        pokemons = []

        for row in pokemon_rows:
            columns = row.find_all('td')
            pokemon_data = {
                'Number': columns[0].text.strip(),
                'Name': columns[1].text.strip().lower(),
                'Type': columns[2].text.strip(),
                'Total': columns[3].text.strip(),
                'HP': columns[4].text.strip(),
                'Attack': columns[5].text.strip(),
                'Defense': columns[6].text.strip(),
                'Sp. Atk': columns[7].text.strip(),
                'Sp. Def': columns[8].text.strip(),
                'Speed': columns[9].text.strip()
            }
            pokemons.append(pokemon_data)

        return pokemons, None
    except Exception as e:
        return None, str(e)

@bot.command("pokemon")
async def find_pokemon(ctx, name: str):
    pokemons, error = fetch_pokemon_data()

    if error:
        await ctx.send(f"An error occurred while fetching Pokémon data: {error}")
        return

    name = name.lower()
    for poke in pokemons:
        if poke['Name'] == name:
            await ctx.send(f"Details for {name.capitalize()}:\n" + "\n".join([f"{key}: {val}" for key, val in poke.items()]))
            return
    await ctx.send(f"Could not find a Pokémon named {name.capitalize()}.")

bot.run(DISCORD_TOKEN)

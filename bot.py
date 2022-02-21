import os
from urllib import response
import random
import requests
import json
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if(message.author)==client.user:
        return
    
    if(message.content == '!random'):
        response = random.randint(0,100)
        await message.channel.send(response)
    
    if(message.content == '!quote'):
        response = get_quote()
        await message.channel.send(response)


client.run(TOKEN)
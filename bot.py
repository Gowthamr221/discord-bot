import os
from urllib import response
import random
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

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


client.run(TOKEN)
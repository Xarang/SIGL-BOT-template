import os
import discord
from discord import message
from discord.ext import commands

from dotenv import load_dotenv

from name import handle_name
from count import handle_count

load_dotenv()
intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():  # When the bot is ready
    print("Connected to Discord")

@client.event
async def on_message(message):

    if not message.content.startswith('!'):
        return
    res = await handle_name(message)
    res = await handle_count(message, client)
    print(res)




client.run(os.getenv('DISCORD_BOT_TOKEN'))

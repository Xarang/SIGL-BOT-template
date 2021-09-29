import os
import discord
from discord import message
from discord.ext import commands

from dotenv import load_dotenv

from name import handle_name

load_dotenv()

client = discord.Client()

@client.event
async def on_ready():  # When the bot is ready
    print("Connected to Discord")

@client.event
async def on_message(message):

    if not message.content.startswith('!'):
        return
    res = await handle_name(message)
    print(res)




client.run(os.getenv('DISCORD_BOT_TOKEN'))

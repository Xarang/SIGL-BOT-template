import os
import discord
from discord import message
from discord.ext import commands

from dotenv import load_dotenv

"""
bot = commands.Bot(
    command_prefix="!",  # Change to desired prefix
    case_insensitive=True  # Commands aren't case-sensitive
)

bot.author_id = 0000000  # Change to your discord id!!!

@bot.event
async def on_ready():  # When the bot is ready
    print("I'm in")
    print(bot.user)  # Prints the bot's username and identifier

@bot.command()
async def pong(ctx):
    await ctx.send('pong')
"""

load_dotenv()

client = discord.Client()

@client.event
async def on_ready():  # When the bot is ready
    print("Connected to Discord")

@client.event
async def on_message(message):

    if not message.content.startswith('!'):
        return

    author = message.author
    if message.content == '!name':
        await message.channel.send(author)


client.run(os.getenv('DISCORD_BOT_TOKEN'))


"""
token = "<MY_SUPER_TOKEN>"
bot.run(token)  # Starts the bot
"""
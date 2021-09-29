import os
import discord
from discord.ext import commands


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


SERVER_ID = '892819997221593178'
APPLICATION_ID = '892821665585700935'
APPLICATION_PUBLIC_KEY = '88c0481520699f2496e165e6c42702e9024ac8c82fc97166b8542a6d1f719316'
DISCORD_BOT_TOKEN = 'ODkyODIxNjY1NTg1NzAwOTM1.YVSe-A.ehi3Cp9Dcv6Y-oL_TyJg_ai7NfY'

client = discord.Client()

@client.event
async def on_ready():  # When the bot is ready
    print("I'm in")
    print(client.user)  # Prints the bot's username and identifier

@client.event
async def on_message(message):

    if not message.content.startswith('!'):
        return

    author = message.author
    if message.content.startswith('!admin'):
        await message.channel.send(author.user)


client.run(DISCORD_BOT_TOKEN)


"""
token = "<MY_SUPER_TOKEN>"
bot.run(token)  # Starts the bot
"""
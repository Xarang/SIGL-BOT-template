import os
import discord
from discord import message
from discord.ext import commands

from dotenv import load_dotenv

from name import handle_name

load_dotenv()

#client = discord.Client()


bot = commands.Bot(command_prefix='!')

@commands.command(name='name')
async def on_message(ctx):
    await ctx.channel.send(ctx.author)

bot.add_command(handle_name)

bot.run(os.getenv('DISCORD_BOT_TOKEN'))

#client.run(os.getenv('DISCORD_BOT_TOKEN'))

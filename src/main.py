import os
import discord
from discord import message
from discord.ext import commands

from dotenv import load_dotenv

from name import handle_name
from count import handle_count
from xkcd import handle_xkcd
from poll import handle_poll

load_dotenv()
intents = discord.Intents.default()
intents.members = True
intents.presences = True

bot = commands.Bot(command_prefix='!', intents=intents)

@commands.command(name='name')
async def on_message(ctx):
    await ctx.channel.send(ctx.author)

bot.add_command(handle_name)
bot.add_command(handle_count)
bot.add_command(handle_xkcd)
bot.add_command(handle_poll)
bot.run(os.getenv('DISCORD_BOT_TOKEN'))
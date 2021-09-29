import os
import discord
from discord import message
from discord.ext import commands

from dotenv import load_dotenv

from name import handle_name
from count import handle_count
from admin import handle_admin
from xkcd import handle_xkcd
from mute import handle_mute

load_dotenv()
intents = discord.Intents.default()
intents.members = True
intents.presences = True


bot = commands.Bot(command_prefix='!', intents=intents)

bot.add_command(handle_name)
bot.add_command(handle_count)
bot.add_command(handle_admin)
bot.add_command(handle_xkcd)
bot.add_command(handle_mute)
bot.run(os.getenv('DISCORD_BOT_TOKEN'))

#client.run(os.getenv('DISCORD_BOT_TOKEN'))

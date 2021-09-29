from logging import log
from discord.ext import commands
import random
import discord

@commands.command("xkcd")
async def handle_xkcd(ctx,):
    messages = ["https://imgs.xkcd.com/comics/flies.png", "https://imgs.xkcd.com/comics/wrong_superhero.png ", "https://imgs.xkcd.com/comics/size_venn_diagram.png", "https://imgs.xkcd.com/comics/dPain_over_dt.png"]
    await ctx.send(random.choice(messages))

from logging import log
from discord import message
from discord.ext import commands
import random
import discord

def parseQuestion(args):
    res = ""
    i = 0
    for arg in args:
        res += arg
        if arg == '?' or arg[:-1] == '?':
            return (res, i)
        i += 1
        return ("Bad format", -1)
        
        

@commands.command("poll")
async def handle_poll(ctx, *args):
    if args is None:
        return 
    question, returnValue = parseQuestion(args)
    if returnValue == -1:
        await ctx.send("error, bad format")

    msg = await ctx.send("@here\n" + question)
    if len(args) == 1:
        await msg.add_reaction("👍")
        await msg.add_reaction("👎")
    # elif len
    # else:
        # await ctx.send("error")

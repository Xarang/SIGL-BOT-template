from logging import log
from discord.ext import commands
import discord

@commands.command("count")
async def handle_count(ctx,):
    offlineMembers = ""
    onlineMembers = ""
    idleMembers = ""
    dndMembers = ""
    for member in ctx.guild.members:
        print(member.status)
        if member.status == discord.Status.offline:
            offlineMembers += member.name + '\n'
        elif member.status == discord.Status.online:
            onlineMembers += member.name + '\n'
        elif member.status == discord.Status.idle:
            idleMembers += member.name + '\n'
        elif member.status == discord.Status.dnd or member.status == discord.Status.do_not_disturb:
            dndMembers += member.name + '\n'
    msg = "Online\n==============\n" + onlineMembers + "\n==============\nOffline\n==============\n" + offlineMembers + "\n==============\nIdle\n==============\n" + idleMembers
    await ctx.channel.send(msg)
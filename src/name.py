from discord.ext import commands

@commands.command(name='name')
async def handle_name(ctx):
    await ctx.channel.send(ctx.author)

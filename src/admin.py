from discord.ext import commands
from discord import Permissions, member, permissions

from utils import get_member

@commands.command(name='admin')
async def handle_admin(ctx, name_or_id):
    guild = ctx.guild
    search_role = list(filter(lambda role: role.name == "Admin", guild.roles))
    if (len(search_role) != 0):
        print("role Admin already exists")
    else:
        await guild.create_role(name="Admin", permissions=Permissions.all()) #TODO: make permissions less permissive
        print("created Admin role")
    member = get_member(guild, name_or_id)
    if not member:
        print("could not get server member: " + name_or_id)
    else:
        search_role = list(filter(lambda role: role.name == "Admin", guild.roles))
        #admin_role = list(filter(lambda role: guild.roles
        await member.add_roles(search_role[0])
        print("added Admin role to " + name_or_id)


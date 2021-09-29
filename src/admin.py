from discord.ext import commands
from discord import Permissions, member, permissions

@commands.command(name='admin')
async def handle_admin(ctx, arg1):
    guild = ctx.guild
    search_role = list(filter(lambda role: role.name == "Admin", guild.roles))
    if (len(search_role) != 0):
        print("role Admin already exists")
    else:
        await guild.create_role(name="Admin", permissions=Permissions.all()) #TODO: make permissions less permissive
        print("created Admin role")
    search_member = list(filter(lambda member: member.name == arg1, guild.members))
    if (len(search_member) == 0):
        print("could not get server member: " + arg1)
    else:
        search_role = list(filter(lambda role: role.name == "Admin", guild.roles))
        #admin_role = list(filter(lambda role: guild.roles
        await search_member[0].add_roles(search_role[0])
        print("added Admin role to " + arg1)


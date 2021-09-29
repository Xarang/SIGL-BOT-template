from discord.ext import commands
from discord import Permissions, member, permissions

@commands.command(name='mute')
async def handle_mute(ctx, arg1):
    guild = ctx.guild
    search_role = list(filter(lambda role: role.name == "Ghost", guild.roles))
    if (len(search_role) != 0):
        print("role Ghost already exists")
    else:
        await guild.create_role(name="Ghost", permissions=Permissions(send_messages=False))
        print("created Ghost role")
    search_member = list(filter(lambda member: member.name == arg1, guild.members))
    if (len(search_member) == 0):
        print("could not get server member: " + arg1)
    else:
        search_role = list(filter(lambda role: role.name == "Ghost", guild.roles))
        member = search_member[0]
        search_member_roles = list(filter(lambda role: role.name == "Ghost", member.roles))
        if len(search_member_roles) == 0:
            await search_member[0].add_roles(search_role[0])
            print("added Ghost role to " + arg1)
        else:
            await search_member[0].remove_roles(search_role[0])
            print("removed Ghost role from " + arg1)


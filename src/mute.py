from discord.ext import commands
from discord import Permissions, member, permissions


from utils import get_member

@commands.command(name='mute')
async def handle_mute(ctx, name_or_id):
    guild = ctx.guild
    search_role = list(filter(lambda role: role.name == "Ghost", guild.roles))
    if (len(search_role) != 0):
        print("role Ghost already exists")
    else:
        await guild.create_role(name="Ghost", permissions=Permissions(send_messages=False))
        print("created Ghost role")
    member = get_member(guild, name_or_id)
    if member:
        search_role = list(filter(lambda role: role.name == "Ghost", guild.roles))
        search_member_roles = list(filter(lambda role: role.name == "Ghost", member.roles))
        if len(search_member_roles) == 0:
            await member.add_roles(search_role[0])
            print("added Ghost role to " + name_or_id)
        else:
            await member.remove_roles(search_role[0])
            print("removed Ghost role from " + name_or_id)


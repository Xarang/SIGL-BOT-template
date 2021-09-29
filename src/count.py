from logging import log

import discord


async def handle_count(message, client):
    if message.content == '!count':
        members = client.get_all_members()

        offlineMembers = ""
        onlineMembers = ""
        idleMembers = ""
        dndMembers = ""
        for member in members:
            print(member.status)
            if member.status == discord.Status.offline:
                offlineMembers += member.name + '\n'
            elif member.status == discord.Status.online:
                onlineMembers += member.name + '\n'
            elif member.status == discord.Status.idle:
                idleMembers += member.name + '\n'
            elif member.status == discord.Status.dnd or member.status == discord.Status.do_not_disturb:
                dndMembers += member.name + '\n'
        msg = "\nOnline\n==============\n" + onlineMembers + "Offline\n==============\n" + offlineMembers + "Idle\n==============\n"
        # print(msg)
        await message.channel.send(msg)
        return True
    return False
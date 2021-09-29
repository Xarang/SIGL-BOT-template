def get_member(guild, name_or_id):
    if name_or_id[0] == '<': #someone was mentionned...
        search_member = list(filter(lambda member: ('<@!' + str(member.id) + '>') == name_or_id, guild.members))
        if (len(search_member) == 0):
            print("could not get server member: '" + name_or_id + "'")
            return None
        else:
            return search_member[0]
    else: #someone was mentionned...
        search_member = list(filter(lambda member: member.name == name_or_id, guild.members))
        if (len(search_member) == 0):
            print("could not get server member: " + name_or_id)
            return None
        else:
            return search_member[0]
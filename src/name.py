
async def handle_name(message):
    if message.content == '!name':
        await message.channel.send(message.author)
        return True
    return False

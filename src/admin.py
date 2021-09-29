
async def handle_admin(message):
    if message.startswith('!admin'):
        print(message)
        return True
    return False
async def main(message, client, args):
    await client.send_message(message.channel, "Hello, world")
async def help(message, client, args):
    await client.send_message(message.channel, "Help for " + args[1] + ":")
    await client.send_message(message.channel, "Says hello to you and the rest of the world")
    await client.send_message(message.channel, "Usage: !hello")
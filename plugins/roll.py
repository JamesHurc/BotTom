from random import randint
async def main(message, client, args):
    if len(args[1]) > 1:
        args[1] = args[1][1:]
        try:
            args[1] = int(args[1])
        except Exception as exception:
            await client.send_message(message.channel, "An error occoured")
            log("Command roll had error " + exception)
        args[1] = float(args[1])
        await client.send_message(message.channel, randint(1, args[1]))
    else:
        await client.send_message(message.channel, "You must specify a number, e.g. d4")


async def help(message, client, args):
    await client.send_message(message.channel, "Roll allows for rolling a dice of a specific (positive integer) number of sides")
    await client.send_message(message.channel, "Usage: !roll d[Number]")

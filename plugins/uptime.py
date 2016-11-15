import time, datetime

starttime = time.time()

async def main(message, client, args):
    uptime = time.time() - starttime
    uptime = datetime.timedelta(seconds=int(uptime))
    await client.send_message(message.channel, "Current uptime is: " + str(uptime))

async def help(message, client, args):
    await client.send_message(message.channel, "Help for " + args[1] + ":")
    await client.send_message(message.channel, "Displays the uptime of the bot")
    await client.send_message(message.channel, "Usage: !uptime")
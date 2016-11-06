import json
async def main(message, client, config, Discord):

    await addReaction(message, client, config, Discord) # Check for reactions

async def addReaction(message, client, config, Discord):
    for react in config["reactions"]:
        if react["trigger"].lower() in message.content.lower():
            await client.add_reaction(message, react["react"])
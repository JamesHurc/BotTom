import json
async def main(message, client, config, Discord):

    await addReaction(message, client, config, Discord) # Check for reactions
    await automatedReply(message, client, config) # Check for automatedReplies

async def addReaction(message, client, config, Discord):
    for react in config["reactions"]:
        if react["trigger"].lower() in message.content.lower():
            await client.add_reaction(message, react["react"])

async def automatedReply(message, client, config):
    for automatedReply in config["automatedReplies"]:
        if automatedReply["trigger"].lower() in message.content.lower():
            await client.send_message(message.channel, automatedReply["response"])
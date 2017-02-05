import json
async def main(message, client, config, Discord):

    await addReaction(message, client, config, Discord) # Check for reactions
    await automatedReply(message, client, config) # Check for automatedReplies

async def addReaction(message, client, config, Discord):
    for react in config["reactions"]:
        if react["trigger"].lower() in message.content.lower():
            await client.add_reaction(message, react["react"])
            log("Reaction " + react["react"] + " was added to the message " + message.content, 1)

async def automatedReply(message, client, config):
    for automatedReply in config["automatedReplies"]:
        if automatedReply["trigger"].lower() in message.content.lower():
            await client.send_message(message.channel, automatedReply["response"])

async def help(message, client, args):
    await client.send_message(message.channel, "This is the auto module. Essentially it's a tonne of triggers that automatically respond to every mesasge you write. It can be configured to reply automatically, add reactions to messages, and maybe more things in the future. To configure it edit the autoConfig.json file.")

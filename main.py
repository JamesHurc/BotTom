import importlib, os, discord, asyncio, json, builtins, utilities

client = discord.Client() #Set the client
plugins = {} #Set plugins to empty

builtins.log = utilities.log #Import logging from the utilities file
builtins.getCommandTable = utilities.getCommandTable

with open('config.json') as json_data_file: #Open the config json file
    data = json.load(json_data_file)

with open('autoConfig.json') as json_data_file: # Open the configuration for auto, a module allowing for reactions etc
    autoConfig = json.load(json_data_file)

def loadPluginFromLocal(name): #Local is the name of the file with the file extension on the end.
    log("Found, and attempting to load file " + name, 1)
    if name not in data["modulesToIgnore"]:
        try:
            pluginFinalName = name.split(".")
            obj = importlib.import_module("plugins." + pluginFinalName[0])
            plugins[pluginFinalName[0]] = obj
            log("Plugin " + name + " was succesfully loaded", 2)
        except Exception as exception:
            log("Plugin " + name + " was not loaded as " + exception, 3)
    elif name in data["modulesToIgnore"]:
        log("Plugin " + name + " was not loaded, due to being ignored in config", 2)
    else:
        log("Plugin " + name + "was not loaded, for an unknown reason", 3)

def searchAndLoad():
    contents = os.listdir("plugins")
    for toLoad in contents:
        if toLoad.endswith('.py'):
            loadPluginFromLocal(toLoad)

async def handleIncoming(message):
    if message.author.id != client.user.id and message.content.startswith(data["cmdStart"]): #Check to make sure that the bot is not responding to its own message
        commTbl = getCommandTable(message.content)
        await handleIncomingCommand(message, commTbl)
    elif message.author.id != client.user.id:
        await plugins['auto'].main(message, client, autoConfig, discord)

async def handleIncomingCommand(message, commTbl):
    if commTbl[0].lower() == "help":
        if len(commTbl) == 1:
            await client.send_message(message.channel, "The following plugins are loaded:")
            for plugin in plugins:
                await client.send_message(message.channel, "• " + str(plugin).title())
            await client.send_message(message.channel, "Use !help <command> to find out more about a specific command")
        elif commTbl[1].lower() in plugins:
            log("Attempting to run help on command " + commTbl[1], 1)
            try:
                await plugins[commTbl[1].lower()].help(message, client, commTbl)
            except Exception as exception:
                await client.send_message(message.channel, "An error occoured while looking for help")
                log("An error occured within help for " + commTbl[1] + exception)
        elif commTbl[1].lower() == "help":
            await client.send_message(message.channel, "Oh aren't you clever calling help on help to see what happens. Well done.")
        else:
            await client.send_message(message.channel, "Help for command " + commTbl[1] + " could not be found. No plugin named" + commTbl[1] + " was loaded.")
    elif commTbl[0].lower() in plugins:
        try:
            await plugins[commTbl[0].lower()].main(message, client, commTbl)
            log("Attempting to run command " + commTbl[0], 1)
        except Exception as ex:
            log("An error occurred within '" + commTbl[0] + "': " + str(ex), 3)
    else:
        await client.send_message(message.channel, "Command not recognised.")
        log("An eror occoured, command " + "'" + commTbl[0] + "'" + " was not recognised", 3)

@client.event #When a message is received.
async def on_message(message):
    await handleIncoming(message)

@client.event #When the bot has loaded.
async def on_ready():
    log("Logged in as " + client.user.name + " and loaded all plugins", 2)
    await client.change_presence(game=discord.Game(name=data["currentlyPlaying"]))


searchAndLoad() #Load modules
client.run(data["token"])
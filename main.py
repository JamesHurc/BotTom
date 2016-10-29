import importlib, os, discord, asyncio, json, builtins, utilities

ignoreNames = ["__pycache__", "__init__.py"] #Define file names to ignore when loading modules
client = discord.Client() #Set the client
plugins = {} #Set plugins to empty

builtins.log = utilities.log #Import logging from the utilities file

with open('config.json') as json_data_file: #Open the config json file
    data = json.load(json_data_file)

def loadPluginFromLocal(name): #Local is the name of the file with the file extension on the end.
    log("Attempting to load module " + name, 2)
    pluginFinalName = name.split(".")
    obj = importlib.import_module("plugins." + pluginFinalName[0])
    plugins[pluginFinalName[0]] = obj

def searchAndLoad():
    contents = os.listdir("plugins")
    for toLoad in contents:
        if toLoad not in ignoreNames:
            loadPluginFromLocal(toLoad)

def getCommandTable(comm):
    comm = comm[1:]
    commTbl = comm.split(" ")
    return commTbl

async def handleIncomingCommand(message):
    if message.author.id != client.user.id and message.content.startswith(data["cmdStart"]): #Check to make sure that the bot is not responding to its own message
        commTbl = getCommandTable(message.content)
        if commTbl[0] in plugins:
            try:
                await plugins[commTbl[0]].main(message, client, commTbl)
                log("Attempting to run command " + commTbl[0], 1)
            except Exception as ex:
                log("An error occurred within '" + commTbl[0] + "': " + str(ex), 3)
        else:
            await client.send_message(message.channel, "Command not recognised.")
            log("An eror occoured, command " + "'" + commTbl[0] + "'" + " was not recognised", 3)

@client.event #When a message is received.
async def on_message(message):
    await handleIncomingCommand(message)

@client.event #When the bot has loaded.
async def on_ready():
    log("Logged in as " + client.user.name + " and loaded all plugins", 2)


searchAndLoad() #Load modules
client.run(data["token"])
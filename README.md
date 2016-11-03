# BotTom
A Discord Bot that supports user made modules in a nice friendly way (ish)

## How do I use this?

It's pretty simple. Just dowload it in some way, edit the config file to your prefrences, and put the token for your discord bot into the token part, and then run main.py (or start.bat). Easy.

### The config file

```{
    "logLevel": 2,
    "token": "insert_token_here",
    "cmdStart": "!",
    "currentlyPlaying": "With his BotTom",
    "modulesToIgnore":[
        "example.py"
    ]
}```

 - logLevel decides the level of log messages you see in the terminal window. A logLevel of 1 will show all messages, 2 important messages and 3 only urgent messages
 - token is the login token the bot requires
 - cmd start is the symbol that signifies the start of a command
 - currentlyPlaying allows you to change what game the bot is showing as playing
 - modulesToIgnore allows you to specify modules not to load

## Contributing & conventions

The bot is pretty receptive to plugins (modules). As currently, a plugin is treated as a command, and will run when somebody perfomd `!plugin_name`. A simple plugin is shown below, which upon `!hello` will output "Hello, world":

```
#hello.py

async def main(message, client, args):
	await client.send_message(message.channel, "Hello, world")
```

The log functionality allows for a message to be outputted to the terminal window that the program is running on. The log command woaks as so

```
log("This is a debug message", 1)

log("This is a helpful message", 2)

log("This is an urgent error do something!", 3)
```

Essentially, the first should be used for any old message a user doesn't need to see. Think something you would only ever need in debugging. The second level for a message that is fairly important, but not realated to a failure of the program. The third level should be used to report errors.

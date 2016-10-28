# BotTom
A Discord Bot that supports user made modules in a nice friendly way (ish)

## How do I use this?

It's pretty simple. Just dowload it in some way, edit the config file to your prefrences, and put the token for your discord bot into the token part, and then run main.py (or start.bat). Easy.

## How do I use my own plugin?

The bot is pretty receptive to plugins (modules). As currently, a plugin is treated as a command, and will run when somebody perfomd `!plugin_name`. A simple plugin is shown below, which upon `!hello` will output "Hello, world":

```
#hello.py

async def main(message, client, args):
	await client.send_message(message.channel, "Hello, world")
```

## Contributing

The code isn't the nicest in places, and if you want to help out, feel free to sumbit a pull request. 

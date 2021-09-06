# MinecraftServerStatusDiscordBot (MSSB)
MinecraftServerStatusDiscordBot or MinecraftServerStatusBot or simply MSSB is a simple bot for displaying the player count and other things of a Minecraft server in Discord, setup is super fast and the bot can easily be self hosted.

# Setup
## 1. Installation
Start by cloning the repository with `git clone` or downloading it as a zip file and extracting it.

## 2. Dependencies
Download the required dependencies with:
```
pip install -r requirements.txt
```
> ⚠️ You might have to replace `pip` with `pip3` depending on your system configuration.

## 3. Configuration
Rename the `.env.example` file to `.env` start filling in the relevant info.
 - `DISCORD_TOKEN` is for your Discord bot token, make a bot then get the token [here](https://discord.com/developers/applications).
 - `SERVER_HOST` The address of your Mineraft server, can include the port afterwards prefix with a `:`.
 - `BOT_PREFIX` The prefix for bot commands in Discord, defaults to `?`.
 - `COLOR_HEX` Hexadecimal format color for the embed, defaults to Discord blurple.

 ## 4. Running
 Simply start the bot with:
 ```
 python main.py
 ```
 > ⚠️ Once again you might have to replace `python` with `python3` depending on your system configuration.
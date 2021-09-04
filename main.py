import logging, discord, os
import discord.ext.tasks as tasks
import discord.ext.commands as commands
from dotenv import load_dotenv
from mcstatus import MinecraftServer
from typing import Optional, TypeVar

logging.basicConfig(level=logging.INFO)

# Rust style unwrap method that throws if value is None
T = TypeVar("T")
def unwrap(value: Optional[T]) -> T:
    if value is not None:
        return value
    else:
        raise TypeError()

load_dotenv()
DISCORD_TOKEN = unwrap(os.getenv("DISCORD_TOKEN"))
SERVER_HOST = unwrap(os.getenv("SERVER_HOST"))
SERVER_PORT = int(unwrap(os.getenv("SERVER_PORT")))
BOT_PREFIX = unwrap(os.getenv("BOT_PREFIX"))

server = MinecraftServer(SERVER_HOST, SERVER_PORT)
state = server.status()

bot = commands.Bot(command_prefix = BOT_PREFIX)

@bot.event
async def on_ready():
    logging.info(f"Connected to discord")
    update_state.start()

# Command that sends the current server status as an embed
@bot.command()
async def status(ctx: commands.Context):
    logging.info(f"Received status command from {ctx.author}")
    global state
    embed = discord.Embed(
        title = "Status", 
        description = f"{state.players.online} out of {state.players.max} currently online.", 
        color = 0xffb3ff
    )
    embed.add_field(
        name = "Players",
        # List comprehension to get all the players in a nice looking string.
        value = ", ".join([player.name for player in unwrap(state.players.sample)]))

    await ctx.reply(embed=embed)

# Loop that updates the server state and sets the bots presence to match
@tasks.loop(seconds=60)
async def update_state():
    logging.debug("Updating state")
    global state
    state = server.status()
    
    await bot.change_presence(
        activity=discord.Activity(
            type = discord.ActivityType.watching, 
            name = f"{state.players.online} out of {state.players.max} players"
        ))

bot.run(DISCORD_TOKEN)
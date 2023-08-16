#dependancies 


import asyncio
import discord 
import os

from discord.ext import commands
from webbrowser import get

#keys for api's
from apiKeys import *

intents = discord.Intents.all()
intents.members = True

client = commands.Bot(command_prefix = '!', intents=intents)

#console log when running
@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game("mind yer own"))
    print("I'm ready, I'm ready!")

cog_extensions = []

async def load_extensions():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            cog_extensions.append("cogs." + filename[:-3])

    if __name__ == '__main__':
        for extension in cog_extensions:
            await client.load_extension(extension)


async def main():
    async with client:
        await load_extensions()
        await client.start(bot_token)

asyncio.run(main())

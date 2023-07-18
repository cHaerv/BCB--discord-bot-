import discord 
from discord.ext import commands

client = commands.Bot(command_prefix = '!', intents=discord.Intents.all())

@client.event
async def on_ready():
    print("im ready, im ready!")

@client.command()
async def hello(ctx):
    await ctx.send("alright am ya?")

client.run('MTEzMDgyODUxMDQ4NzkyNDc3Nw.Gj9uP1.WeiuPjdvZPDMlCQ8YvQS6vP4AV3XSR6eF7H4Tk')

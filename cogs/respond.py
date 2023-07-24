import discord
from discord.ext import commands


class Respond(commands.Cog):

    def __init__(self, client):
        self.client = client 
    
    #detect words in messages.
    @commands.Cog.listener()
    async def on_message(self, message):
        match message.content:
            case "f":
                await message.channel.send("Big F!")
            case "es ist mir scheiss egal":
                await message.channel.send(f"{message.author.mention} Stop Spaking germin!")
            case "happy birthday":
                await message.channel.send("Merry birthmas and a happy 'nother year!")
            case "west midlands":
                await message.channel.send("west mids best mids mucka!")
            case "godverdomme":
                await message.channel.send(f"{message.author.mention} its all dutch to me mate.")
            case "poggers":
                await message.channel.send(f"Think you mean pukka like the pie {message.author}")

async def setup(client):
    await client.add_cog(Respond(client))
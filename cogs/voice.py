
import discord
import random
from discord.ext import commands


class Voice(commands.Cog):

    def __init__(self, client):
        self.client = client 

    #join voice channel
    @commands.command(parse_context = True)
    async def join(self, ctx):
        voice_chan = discord.utils.get(self.client.voice_clients, guild=ctx.guild) #get the voice channel user is in
        if(voice_chan != None):
            await ctx.send("Am already 'ere ya numpty")
        elif (ctx.author.voice):
            await ctx.send("I'm joining ya call mush")
            channel = ctx.message.author.voice.channel
            await channel.connect()
        else:  
            await ctx.send("You must be in a voice channel for me to join! Ay it")

    #leave voice channel
    @commands.command(parse_context = True)
    async def leave(self, ctx):
        if (ctx.voice_client): 
            await ctx.voice_client.disconnect()
            await ctx.send("I'm gooin ay I")
        else:
            await ctx.send("I cor leave if I ay even there!")

    #play spotify
    
    @commands.command(parse_context = True)
    async def play(self, ctx):
        print("ello")


async def setup(client):
    await client.add_cog(Voice(client))


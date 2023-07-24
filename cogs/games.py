import discord
import random
from discord.ext import commands


class Games(commands.Cog):

    def __init__(self, client):
        self.client = client 
    
    #roll a die
    @commands.command()
    async def roll(self, ctx):
        await ctx.send(random.randint(1,6))

    #roll a d20
    @commands.command()
    async def d20(self, ctx):
        await ctx.send(random.randint(1,20))

    #flip a coin
    @commands.command()
    async def coin_flip(self, ctx):
        await ctx.send(random.choice(["Heads","Tails"]))
    
    #nominates an online non bot user
    @commands.command()
    async def nominate(self, ctx):
        online_members = [] 
        for member in ctx.guild.members:
            if member.bot is False and member.status is not discord.Status.offline: #detect user is not a bot and is online
                online_members.append(member)
            
        chosen_one = random.choice(online_members)
        await ctx.send(f"Arr nominate {chosen_one.mention}!")



async def setup(client):
    await client.add_cog(Games(client))
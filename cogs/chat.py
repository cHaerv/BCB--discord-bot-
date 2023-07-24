import discord
import random
from discord.ext import commands


class Chat(commands.Cog):

    def __init__(self, client):
        self.client = client 

    #say hello
    @commands.command()
    async def hello(self, ctx):
        await ctx.send("Alright am ya?")
    
    #say how are you?
    @commands.command()
    async def how_do(self, ctx):
        await ctx.send("Bostin tarr, and yow?")

    #say goodbye
    @commands.command()
    async def bye(self, ctx):
        await ctx.send("Tararabit!")
    
    #say greeting message
    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = self.client.get_channel(1130866831687688204)
        await channel.send(f"How do {member.mention}? Welcome!")

    #say mitchell quote
    @commands.command()
    async def mitch_gpt(self, ctx):
        mitchQuotes = ["Thats kinda cursed ngl king", "That tone is siiiiiiiiick", "Thats Goated cant lie", "Halo infinite?", "THAT'S HEIIIIINOUS MAN", 
                   "cant talk recording rn soz", "brb bby *dissappears forever leaving no trace on entropy or time", "Aw hells yea", "Uh, so I just think Beserk addresses trauma in a really mature manner", 
                   "Brain go brrr", "that's clapped", "Ay up sonny g", "Strandberg endorsement when?", "Iphone's are clapped bro", "f", "Evangellion is the G.O.A.T", 
                   "*no one literally not a soul.... *mitch: ahahahaha","HENCH HENCH", "Jason richardson is just hench af", f"GOOOOD SAAAKE {ctx.message.author}", f"What dya want noooooooow {ctx.message.author}"]
        chosenQuote = random.choice(mitchQuotes)
        await ctx.send(f"{chosenQuote}")
    
    #say greeting message
    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = self.client.get_channel(1130866831687688204)
        await channel.send(f"How do {member.mention}? Welcome!")

async def setup(client):
    await client.add_cog(Chat(client))


import discord
import random
from discord.ext import commands


class Error(commands.Cog):

    def __init__(self, client):
        self.client = client 


    #detect errors
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            ctx.send("Yow corr do that, ya dow 'ave permission!")

async def setup(client):
    await client.add_cog(Error(client))
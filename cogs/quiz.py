import discord
import requests
from discord.ext import commands

class Quiz(commands.Cog):
    
    
    def __init__(self, client):
        self.client = client 

    

    @commands.command()
    async def true_false(self, ctx):
        difficulty = ctx.message.content.split(" ")[1] if len(ctx.message.content.split(" ")) == 2  else "medium"

        URL = f"https://opentdb.com/api.php?amount=1&category=9&difficulty={difficulty}&type=boolean"
        response = requests.get(URL, headers={'Accept': 'application/json'}).json()
        question = response.get("results")[0]["question"].replace("&quot", "'")
        answer = response.get("results")[0]["correct_answer"]
        await ctx.send(f"True or False? {question}")
        print(answer)
        
        # wait for the answer
        client_ans = await self.client.wait_for('message', timeout=60.0)
        
        #checks if you got the answer correct
        if client_ans.content.lower() == answer.lower():
            await ctx.send("yowm spot on")
        else:
            await ctx.send("Yam nearly there but no ya wrong")

    @commands.command()
    async def multiple_choice(self, ctx):
        URL = f""


async def setup(client):
    await client.add_cog(Quiz(client))
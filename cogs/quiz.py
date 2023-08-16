import discord
import requests
import random
from discord.ext import commands

class Quiz(commands.Cog):
    
    
    def __init__(self, client):
        self.client = client 


    # asks a true or false question
    @commands.command()
    async def true_false(self, ctx):
        difficulty = ctx.message.content.split(" ")[1] if len(ctx.message.content.split(" ")) == 2  else "medium"

        URL = f"https://opentdb.com/api.php?amount=1&category=9&difficulty={difficulty}&type=boolean"
        response = requests.get(URL, headers={'Accept': 'application/json'}).json() # response from requests doing API call for Json data
        question = response.get("results")[0]["question"].replace("&quot", "'") #parse Json data for the question key
        answer = response.get("results")[0]["correct_answer"] # parse for correct answer
        await ctx.send(f"True or False? {question}") #asks question
        # print(answer)
        
        # wait for the answer
        client_ans = await self.client.wait_for('message', timeout=120.0)
        
        #checks if you got the answer correct
        if client_ans.content.lower() == answer.lower():
            await ctx.send("yowm spot on")
        else:
            await ctx.send("Yam nearly there but no ya wrong")

    @commands.command()
    async def multiple_choice(self, ctx):
        params = ctx.message.content.split(" ")
        difficulty = params[1] if len(params) > 1 else "medium"
        URL = f"https://opentdb.com/api.php?amount=1&difficulty={difficulty}&type=multiple"
        print(params)
        response = requests.get(URL, headers={'Accept': 'application/json'}).json() 

        question = response.get("results")[0]["question"].replace("&quot", "'")
        
        answer = response.get("results")[0]["correct_answer"]
        answers_list = response.get("results")[0]["incorrect_answers"]
        answers_list.append(answer)
        random.shuffle(answers_list)
        
        print(answers_list)
        # print(answers_list)
        await ctx.send(f"{question} Is it a.{answers_list[0]}, b.{answers_list[1]}, c.{answers_list[2]}, d.{answers_list[3]}?") 

        client_ans = await self.client.wait_for('message', timeout=120.0)

        if client_ans.content.lower() == answer.lower():
            await ctx.send("yowm spot on")
        else:
            await ctx.send("Yam nearly there but no ya wrong")

async def setup(client):
    await client.add_cog(Quiz(client))
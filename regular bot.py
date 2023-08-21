import discord
from discord.ext import commands
import time
import random
import asyncio
import requests

headers = {
  "Authorization": "Bearer 3bf4e70fa9c24f76b1313a7b",
  "Content-Type": "application/json"
}

t = int(time.time())
delay = 5

bot = commands.Bot(command_prefix="", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID:{bot.user.id})")

@bot.event
async def on_message(ctx):
    if ctx.channel.id == 1070005943049392288 and ctx.author.id != 1070004143021903953:
        global t
        global delay
        timesince = int(time.time()) - t
        if timesince > delay:
            t = int(time.time())
            delay = 5
            body = {
                "text": f"Message: {ctx.content}\nReply: ",
                "top_p": 1,
                "top_k": 40,
                "temperature": 0.9,
                "repetition_penalty":  1.5,
                "length": 24,
                "bad_words": ["Reply: <br>","User: <br>","&lt;","pic.twitter","#"]
            }
            res = requests.post(
                "https://shared-api.forefront.link/organization/c5msanR2wD70/gpt-j-6b-vanilla/completions/nu0ioh5Mk2wl",
                json=body,
                headers=headers
            )
            completion = res.json()["result"][0]["completion"]

            print(f"Replying to: {ctx.content}")
            print(f'Reply: {completion}')
            await ctx.reply(completion)

bot.run("MTA3MDAwNDE0MzAyMTkwMzk1Mw.GUhepg.C6UIzsjis60jpCTm6EVfsvq7KSIAA1bNo1P-yA")
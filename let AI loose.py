import discord
from discord.ext import commands
import random
import time
import asyncio
import requests
import json

headers = {
  "Authorization": "Bearer 3bf4e70fa9c24f76b1313a7b",
  "Content-Type": "application/json"
}



t = int(time.time())
delay = random.randint(5, 10)

bot = commands.Bot(self_bot = True, command_prefix="")

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID:{bot.user.id})")


@bot.event
async def on_message(message):
    if message.channel.id == 361511298451767297:
        global t
        global delay
        timesince = int(time.time()) - t
        if timesince > delay:
            t = int(time.time())
            delay = random.randint(60, 100)

            body = {
                "text": f"Message: {message.content}\nReply: ",
                "top_p": 1,
                "top_k": 40,
                "temperature": 0.9,
                "repetition_penalty":  1.4,
                "length": 64,
                "bad_words": ["Reply: <br>","User: <br>","&lt;","pic.twitter","#"]
            }
            res = requests.post(
                "https://shared-api.forefront.link/organization/c5msanR2wD70/gpt-j-6b-vanilla/completions/nu0ioh5Mk2wl",
                json=body,
                headers=headers
            )
            print(f"Replying to: {message.content}")
            print(f'Reply: {res.json()["result"][0]["completion"]}')
            async with message.channel.typing():
                await asyncio.sleep(2)
            await message.reply(res.json()["result"][0]["completion"])



bot.run("MTA2ODg5NjM2NjkwMzk1NTU0Ng.Gpci6Q.a_CXabfBiVNc1W47Z6cYfRbVbMoBFYodttzY1k")
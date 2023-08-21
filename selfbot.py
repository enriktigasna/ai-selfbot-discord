import discord
from discord.ext import commands

channels = [361511298451767297, 404440555355897879, 588711260237856793]

bot = commands.Bot(self_bot = True, command_prefix="")


def logData(msg):
    with open("log.txt", "a", encoding="utf-8") as f:
        f.write(msg + "\n")
    print(msg)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID:{bot.user.id})")

@bot.event
async def on_message(message):
    if message.channel.id in channels and message.reference:
        old_message = await message.channel.fetch_message(message.reference.message_id)
        logData("#####")
        logData(f"Message: {old_message.content}")
        logData(f"Reply: {message.content}")

bot.run("MTA2ODg5NjM2NjkwMzk1NTU0Ng.Gpci6Q.a_CXabfBiVNc1W47Z6cYfRbVbMoBFYodttzY1k")
# This is the source code for the discord bot "Neat-Bot"
# This code is written for educational purposes and is not intended to be copied/modified in anyway.
# Code is written under fair-use and is not to be commercialized or used outside of discord-servers.
# Created by JuleNissen. Date: 21.6.2018


import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio

#To send command to this bot user must start command with "§" to be recognised
bot = commands.Bot(command_prefix="§") 

@bot.event
async def on_ready():
	print ("Bot is armed and ready, sir!")
	print ("Line two of print-lines")







#In this version of code the token is NOT implemented for own protection!
bot.run("BOT_TOKEN")
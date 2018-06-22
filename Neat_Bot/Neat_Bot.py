# This is the source code for the discord bot "Neat-Bot"
# This code is written for educational purposes and is not intended to be copied/modified in anyway.
# Code is written under fair-use and is not to be commercialized or used outside of discord-servers.
# Created by JuleNissen. Date: 21.6.2018

import discord
from discord.member import Member
from discord.ext import commands
from discord.ext.commands import Bot
from discord.voice_client import VoiceClient
import asyncio

startup_extensions = ["Music", "Utility"]

#To send command to this bot user must start command with "§" to be recognised
bot = commands.Bot(command_prefix="§")
#client = discord.Client()

@bot.event
async def on_ready():
    print("Bot details: \n------------------------------")
    print(bot.user.name)
    print(bot.user.id)
    print ("Bot is armed and ready, sir!")
    print("------------------------------")
    await bot.change_presence(game=discord.Game(name="Slap my bitch up!"), status=discord.Status("idle"))

#Allow users to request user-info for other users.
@bot.command(pass_context = True)
async def info(ctx, user: discord.Member):
    """Allows user to specify which user to get information about"""
    embed = discord.Embed(title="{}'s info".format(user.name), description="Information on user", color=0xffffff, inline= True)
    embed.add_field(name="Name", value=user.name)
    embed.add_field(name="ID", value=user.id)
    embed.add_field(name="Status", value=user.status)
    embed.add_field(name="Highest role", value=user.top_role)
    embed.add_field(name="Joined", value=user.joined_at)
    embed.set_thumbnail(url=user.avatar_url)
    await bot.say(embed=embed)


#Allow users to get info of server
@bot.command(pass_context = True)
async def serverinfo(ctx):
    """Returns information about the server."""
    embed = discord.Embed(name="{}'s info".format(ctx.message.server.name), description="Information on server", color=0x00ff00, inline = True)
    embed.set_author(name="NSA")
    embed.add_field(name="Name", value=ctx.message.server.name)
    embed.add_field(name="ID", value=ctx.message.server.id)
    embed.add_field(name="Roles", value=len(ctx.message.server.roles))
    embed.add_field(name="Members", value=len(ctx.message.server.members))
    embed.set_thumbnail(url=ctx.message.server.icon_url)
    await bot.say(embed=embed)


#Custom introduction
@bot.command(pass_context = True)
async def introduction(ctx):
    """Let the bot give a short introduction about itself."""
    await bot.say("Hello! \n" + "My name is {}".format(bot.user.name)+"\n"
    + "You can give me commands by using the § sign followed by a command you wish me to fulfill \n"
    + "If you want more info, just type: §help")

#From youtube link: https://www.youtube.com/watch?v=FpRzDY0-I1o 
#Will try to load extensions, will trow error if failure.
if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            exc = "{}: {}".format(type(e).__name__, e)
            print("Failed to load extension {}+n{}".format(startup_extensions, exc))


#In this version of code the token is NOT implemented for own protection!
#TODO: remove/add token ID to make bot function
bot.run("TOKEN")
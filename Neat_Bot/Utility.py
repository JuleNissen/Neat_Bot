#This code represents what the author thinks goes under utility functions.
#Code is meant to work with Neat-Bot.
#Modules need self as argument for each command-funcs.
#NOTE: modules have "self.bot.say" instead of "bot.say" !

import discord
from discord.ext import commands

#Define the word bot.
bot = commands.Bot(command_prefix="§")

class Utility():
    """Class for utility functions"""
    def __init__(self, bot):
        self.bot = bot

    #Allow users in group Admin to kick anyone outside group.
    @bot.command(pass_context = True)
    async def kick(self, ctx, user:discord.Member):
        """Allows user to specify someone to kick from server"""
        await self.bot.say(":eggplant: Begone! {}".format(user.name))
        await self.bot.kick(user)

    #TODO: Allow user to delete last message sent from bot.        
    @bot.command(pass_context = True)
    async def deleteLast(self, ctx, *, msg = None):
        """Delete the last sent message."""
        await self.bot.delete_message(ctx.message)
        await self.bot.say("Just deleted the previous message!:wink:")

#This is nessecary for modules implemented for Neat-Bot
def setup(bot):
    bot.add_cog(Utility(bot))
    print('Utilities is loaded')

import discord
from discord.ext import commands

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
    async def deleteLast(self, ctx, *, msg = 1):
        """Delete the last sent message."""
        await self.bot.delete_message(ctx.message)
        await self.bot.say("Just deleted the previous message!:wink:")

def setup(bot):
    bot.add_cog(Utility(bot))
    print('Utilities is loaded')

    # https://www.youtube.com/watch?v=FpRzDY0-I1o 
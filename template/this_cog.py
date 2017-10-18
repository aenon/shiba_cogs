import discord
from discord.ext import commands

class this_cog:
    """This cog."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def this_cog(self):
        """This cog"""

        await self.bot.say("This is just such a cog!")

def setup(bot):
    bot.add_cog(this_cog(bot))

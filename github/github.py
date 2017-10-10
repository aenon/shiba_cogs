import discord
from discord.ext import commands

class github:
    """This cog checks the information of a repo, user or organization"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def github(self, ghname):
        """checks information"""

        await self.bot.say("This is work in progress!")

def setup(bot):
    bot.add_cog(github(bot))

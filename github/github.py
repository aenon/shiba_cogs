import discord
from discord.ext import commands

class github:
    """Checks the information of a repo, user or organization on github.com"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def github(self, ghname):
        """checks information"""

        await self.bot.say("This is work in progress!")

def setup(bot):
    bot.add_cog(github(bot))

import discord
from discord.ext import commands

class hackernews:
    """Read hackernews"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def hackernews(self):
        """Read hackernews with Red bot"""

        await self.bot.say("This is work in progress!")

def setup(bot):
    bot.add_cog(hackernews(bot))

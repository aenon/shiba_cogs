import discord
import random
from discord.ext import commands

class fortune:
    """fortune related commands."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def fortune(self):
        """Get random fortune
        """

        await self.bot.say("I can do stuff!")


def setup(bot):
    bot.add_cog(fortune(bot))

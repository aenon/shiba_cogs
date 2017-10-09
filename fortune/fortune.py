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
        fortune_text = subprocess.check_output(['fortune'])
        await self.bot.say(fortune_text)


def setup(bot):
    bot.add_cog(fortune(bot))

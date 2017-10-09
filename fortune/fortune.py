import discord
import random
import subprocess
from discord.ext import commands

class fortune:
    """fortune related commands."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def fortune(self):
        """Get random fortune
        """
        fortune_text = str(subprocess.check_output(['fortune'])).replace('\n', ' ').replace('\t', '  ')
        await self.bot.say(fortune_text)


def setup(bot):
    bot.add_cog(fortune(bot))

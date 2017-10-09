import discord
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
        fortune_text = subprocess.check_output(['fortune'])
        fortune_text = fortune_text.decode('utf8')#.replace('\n', '  ').replace('\t', ' ')
        fortune_text = str(fortune_text).replace('\n', '  ').replace('\t', ' ')
        await self.bot.say(fortune_text)


def setup(bot):
    bot.add_cog(fortune(bot))

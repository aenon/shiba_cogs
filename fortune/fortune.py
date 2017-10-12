import discord
import subprocess
from discord.ext import commands

class fortune:
    """fortune related commands."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def fortune(self, flavor = 'default'):
        """Get random fortune
        """
        fortune_text = subprocess.check_output(['fortune'])
        if flavor.strip().lower() in ['cn', 'zh', 'chinese', 'shici']:
            fortune_text = subprocess.check_output(['fortune-zh'])
        fortune_text = fortune_text.decode('utf8')
        fortune_text = str(fortune_text).replace('\n', ' ').replace('\t', '  ')
        fortune_text = str(fortune_text).replace('\x1b[32m', '').replace('\x1b[33m', '').replace('\x1b[m', '')
        await self.bot.say(fortune_text)


def setup(bot):
    bot.add_cog(fortune(bot))

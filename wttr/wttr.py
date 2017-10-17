import discord
import subprocess
from discord.ext import commands

class wttr:
    """Show weather info from wttr.in"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def wttr(self):
        """Show weather"""

        weather = subprocess.check_output(['curl', 'wttr.in'])
        weather = weather.decode('utf-8')
        await self.bot.say(weather)

def setup(bot):
    bot.add_cog(wttr(bot))

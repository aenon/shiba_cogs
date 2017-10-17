import discord
from discord.ext import commands

class wttr:
    """Show weather info from wttr.in"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def wttr(self):
        """Show weather"""

        weather = subprocess.check_output(['curl'])
        weather = weather.encode('utf-8')
        await self.bot.say(weather)

def setup(bot):
    bot.add_cog(wttr(bot))
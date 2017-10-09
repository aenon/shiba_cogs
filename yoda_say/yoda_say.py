import discord
from discord.ext import commands

class yoda_say:
    """May the force be with you"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def yoda_say(self):
        """May the force be with you"""

        await self.bot.say("I can do stuff!")

def setup(bot):
    bot.add_cog(yoda_say(bot))

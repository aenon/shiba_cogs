import discord
from discord.ext import commands

class lucky:
    """Cog for Husky Lucky"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def lucky(self):
        """Cog for Husky Lucky
        instagram https://www.instagram.com/thehuskylucky/
        get random post: description and url"""

        await self.bot.say("This is work in progress!")

def setup(bot):
    bot.add_cog(lucky(bot))

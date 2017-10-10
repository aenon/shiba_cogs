import discord
from discord.ext import commands

class yoda_say:
    """May the force be with you"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def yoda_say(self, sentence):
        """ Credit to Zenadix and muddyfish
        source: https://codegolf.stackexchange.com/questions/68559/
        a-yoda-speaking-challenge-this-is
        """
        t = sentence.split()
        u = ' '.join(t[2:]).rstrip('!.')
        if t[0].lower() in 'i we you he she it they'.split():
            sentence = "{}{}, {} {}.".format(
                u[0].upper(),
                u[1:],
                ['I', t[0].lower()][t[0] != 'I'], 
                t[1])
        await self.bot.say(sentence)

def setup(bot):
    bot.add_cog(yoda_say(bot))

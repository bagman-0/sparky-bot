from discord.ext import commands
from discord.ext.commands import Context
from helpers import checks





class Responses(commands.Cog, name="responses"):
    
    def __init__(self, bot):
        self.bot = bot



    @commands.Cog.listener('on_message')
    async def gm(self, message):
        """
        Someone says gm, we say bork bork
        
        """
        if message.author == self.bot.user or message.author.bot:
            return
        if message.content.lower().find('gm') != -1:
            await message.channel.send('bark bark')

    @commands.Cog.listener('on_message')
    async def iwillpat(self, message):
        """if the wenie boy enters chat

        Args:
            message (some kind of discord.py obj idfk a message or whatever): 
        """
        if message.author == 745044163170402365:
            await message.channel.send("ooooo ooo wienie boy weinie boy")
    
    
    @commands.Cog.listener('on_message')
    async def wrath(self, message):
        """
        Who is Wrath?
        
        """
        if message.author == self.bot.user or message.author.bot:
            return
        if message.content.lower().find('wrath') != -1:
            await message.channel.send('who?')


async def setup(bot):
    await bot.add_cog(Responses(bot))
""""
Copyright © Krypton 2019-2022 - https://github.com/kkrypt0nn (https://krypton.ninja)
Description:
🐍 A simple template to start to code your own and personalized discord bot in Python programming language.

Version: 5.4.2
"""
import discord
from discord.ext import commands
from discord.ext.commands import Context

from helpers import checks
import os
import openai
from dotenv import load_dotenv
from PIL import Image, ImageOps
import numpy as np
from io import BytesIO
import requests
from helpers.gpt_helpers import prep_gpt_image

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")    
# dotenv_path = join(dirname(__file__), '.env')

def crop_image_only_outside(img,tol=0):
    # img is 2D image data
    # tol  is tolerance
    mask = img>tol
    m,n = img.shape
    mask0,mask1 = mask.any(0),mask.any(1)
    col_start,col_end = mask0.argmax(),n-mask0[::-1].argmax()
    row_start,row_end = mask1.argmax(),m-mask1[::-1].argmax()
    return img[row_start:row_end,col_start:col_end]

# Here we name the cog and create a new class for the cog.
class Doggerino(commands.Cog, name="sewers"):
    
    def __init__(self, bot):
        self.bot = bot

    # Here you can just add your own commands, you'll always need to provide "self" as first parameter.
    # @commands.has_role("sewer schemers")
    # @commands.hybrid_command(
    # name="sewers",
    # description="?")
    # async def testt(self, context: Context):
    #     print(context.author.roles)
    #     await context.send()


        # Don't forget to remove "pass", I added this just because there's no content in the method.
    @commands.has_role("sewer schemers")
    @commands.hybrid_command(
        name="plshalp",
        description="This is a testing command that does nothing.")
    async def doggoadvice(self, context: Context):
        """
        This is a testing command that does nothing.

        :param context: The application command context.
        """
        # There are three basic guidelines to creating prompts:

        # Show and tell. Make it clear what you want either through instructions, examples, or a combination of the two. If you want the model to rank a list of items in alphabetical order or to classify a paragraph by sentiment, show it that's what you want.

        # Provide quality data. If you're trying to build a classifier or get the model to follow a pattern, make sure that there are enough examples. Be sure to proofread your examples — the model is usually smart enough to see through basic spelling mistakes and give you a response, but it also might assume this is intentional and it can affect the response.

        # Check your settings. The temperature and top_p settings control how deterministic the model is in generating a response. If you're asking it for a response where there's only one right answer, then you'd want to set these lower. If you're looking for more diverse responses, then you might want to set them higher. The number one mistake people use with these settings is assuming that they're "cleverness" or "creativity" controls.
        pass

        """
        turn the below commented out method into a doggerino fetch dall-e
        """
    # @commands.has_role("sewer schemers")
    # @commands.hybrid_command(
    # name="bags",
    # description="Will make a bag out of you")
    # async def bagperson(self, context: Context, user:discord.User = None):
    #     """
    #     This is a testing command that does nothing.

    #     DALL-E prompts: Text prompt with descriptive focus on surroundings. the more specific the better

    #     :param context: The application command context.
    #     """
    #     if user is None:
    #         avatar_url = str(context.author.display_avatar)
    #     else:
    #         avatar_url = user.display_avatar
    #     name = context.author.name
    #     print(user)
    #     byts = prep_gpt_image(avatar_url, name=str(context.author.name))
    #     await context.send("pls be patient I'm a little slow at this")
    #     response = await openai.Image.acreate_edit(
    #         image=byts,
    #         # mask=open('piglets-now2.png', "rb"),
    #         prompt="The setting is an underground sewer. Sewers are large pipes where different kinds of waste flow. Sewers also contain wires running down the hallway and other things of that nature. A large sewer pipe that has some wires along the sides. Put the photo in that setting.",
    #         n=1,
    #         size='1024x1024', 
    #         )
    #     image_url = response['data'][0]['url']
    #     await context.send(image_url)

# And then we finally add the cog to the bot so that it can load, unload, reload and use it's content.
async def setup(bot):
    await bot.add_cog(Doggerino(bot))

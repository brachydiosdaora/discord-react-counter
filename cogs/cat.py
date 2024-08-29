import discord
import random
import os
from discord.ext import commands

async def find_cat_txt():
    relative_path = "./persistence/cat_links.txt"
    path = os.getcwd()+relative_path
    fp = open(path, 'r+')
    return random.choice(fp.readlines())

class Cat(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    
    @commands.command(name='cat')
    async def send_cat_image(self,ctx):
        link = await find_cat_txt()
        await ctx.send(f'{link}')

async def setup(bot):
    await bot.add_cog(Cat(bot))
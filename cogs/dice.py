import discord
import random
from discord.ext import commands

class Dice(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name="roll")
    async def roll_dice(self, ctx, highest_int=None, amount_to_roll=1):
        rolled_dice = 0

        def __roll(highest_int):
            return random.randint(1,int(highest_int))

        if highest_int is None:
            await ctx.send(f'The correct syntax is: "&roll + <face amount> + Optional:<roll amount>"')
            return
        try:
            while rolled_dice < amount_to_roll:
                rolled_dice = rolled_dice+1
                result = __roll(highest_int)
                await ctx.send(f":game_die: #{rolled_dice}: {result}")
        except:
            print(f"noob")
            await ctx.send(f"i broke")

async def setup(bot):
    await bot.add_cog(Dice(bot))
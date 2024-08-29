import discord
import random
import os
from random import randrange
from dotenv import load_dotenv   
from discord.ext import commands

load_dotenv()
intents = discord.Intents.default() 
intents.message_content = True

bot = commands.Bot(command_prefix="&", intents=intents)

@bot.event
async def on_ready():
    print(f'I AM READY')

@bot.listen('on_message')
async def respond_to_message (message): 
    if message.author == bot.user:
        return
    if message.content.startswith("!trolley"):
        await message.channel.send("push")

@bot.command(name='commands')
async def commandList(ctx):
    await ctx.send(f'List of commands: cat')

@bot.command(name="roll")
async def roll_dice(ctx, highest_int=None, amount_to_roll=1):
    rolled_dice = 0

    def __roll(highest_int):
        return random.randint(1,int(highest_int))

    if highest_int is None:
        await ctx.send(f"The correct syntax is: &{roll_dice.name} + <range of int> + Optional:<times to roll>")
        return
    try:
        while rolled_dice < amount_to_roll:
            rolled_dice = rolled_dice+1
            result = __roll(highest_int)
            await ctx.send(f":game_die: #{rolled_dice}: {result}")
    except:
        print(f"noob")
        await ctx.send(f"i broke")

@bot.command()
async def cat(ctx):
    links = ["https://tenor.com/view/cat-on-fire-sitting-edited-on-fire-fire-gif-17645117","https://cdn.discordapp.com/attachments/954685416655695884/1272496214796927059/catgeon.gif?ex=66d047f3&is=66cef673&hm=a576a3248429b3f388401f29ad6bf6ea4cdc5525163e8addda06b6e05d0bc017&"]
    link = random.choice(links)
    await ctx.send(link)

@bot.command()
async def mog(ctx):
    await ctx.send(f'mog')
    

bot.run(os.getenv('TOKEN'))
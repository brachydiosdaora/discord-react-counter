import discord
import random
import os
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

@bot.command()
async def cat(ctx):
    links = ["https://tenor.com/view/cat-on-fire-sitting-edited-on-fire-fire-gif-17645117","https://cdn.discordapp.com/attachments/954685416655695884/1272496214796927059/catgeon.gif?ex=66d047f3&is=66cef673&hm=a576a3248429b3f388401f29ad6bf6ea4cdc5525163e8addda06b6e05d0bc017&"]
    link = random.choice(links)
    await ctx.send(link)

@bot.command()
async def mog(ctx):
    await ctx.send(f'mog')
    

bot.run(os.getenv('TOKEN'))
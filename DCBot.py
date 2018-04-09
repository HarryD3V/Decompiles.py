#Decompiled's bot
import discord
from discord.ext import commands
from discord.ext.commands import bot
import asyncio

bot = commands.Bot(command_prefix=';')
@bot.event
async def on_ready():
    print("Ready When you are :D")
    print("Built in python by HarryD3V")

@bot.command(pass_context=True)
async def ping(ctx):
    await bot.say(":ping_pong:")
    print ("user has pinged")

@bot.command(pass_context=True)
async def info(ctx, user: discord.Member):
    await bot.say("The users name is: {}".format(user.name))
    await bot.say("The users ID is: {}".format(user.id))
    await bot.say("The users status is: {}".format(user.status))
    await bot.say("The users highest role is: {}".format(user.top_role))
    await bot.say("The user joined at: {}".format(user.joined_at))

@bot.command(pass_context=True)
async def kick(ctx, user: discord.Member):
    await bot.say(":boot: Cya, {}. Ya loser!".format(user.name))
    await bot.kick(user)


@bot.command(pass_context=True)
async def hsay(ctx, *args):
    mesg = ' '.join(args)
    await bot.delete_message(ctx.message)
    return await bot.say(mesg)

@commands.command()
async def whisper(self, *, message):
    await self.bot.whisper(message)


bot.run("NDMyNTI3MDU3ODU1OTcxMzQ5.DauvcA.dwB8KLj5I6PIjPfnYhgOZDWfGiE")
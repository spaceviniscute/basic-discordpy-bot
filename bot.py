import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!')

@bot.command(name='autism', description='ko jos koristi deskripciju')
async def autism(ctx):
    await ctx.send('AUTIZMU!')

bot.run('OD TVOG BOTA AUTISTICNI TOKEN')

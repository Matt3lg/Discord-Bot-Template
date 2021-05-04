import discord
import json
import os
from discord.ext import commands, tasks
from itertools import cycle

token = ('BOT TOKEN')
bot = commands.Bot(command_prefix='l!')

@bot.event
async def on_ready():
    change_status.start()
    print('On')

bot.run(token)

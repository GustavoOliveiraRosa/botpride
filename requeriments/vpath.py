import discord
from discord.ext import commands
import os
import whois

PATH = os.environ['KEY_BOT_DISCORD']
print(PATH)
bot = commands.Bot(command_prefix='$')
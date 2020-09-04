import discord
from discord.ext import commands
import os
import whois

#Importando variáveis de ambientes globais na aplicacao
from requeriments.vpath import *

@bot.command()
async def hacking_whois(ctx, site):
    domain = whois.whois(site)
    await ctx.send(domain)
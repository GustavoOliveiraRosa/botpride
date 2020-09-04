import discord
from discord.ext import commands
import os

#Importando variaveis de ambientes globais na aplicacao
from requeriments.vpath import *

#Importando endpoints
from endpoints.essentials import *
from endpoints.hacking import *
from endpoints.academico import *
from endpoints.watchman import *

#Importando funcao mysql 
from functions.mysql import * 

#Comandos iniciais e essenciais do bot
client = discord.Client()

@bot.event
async def on_ready():
    print('Logado como: ')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.event
async def on_command_error(ctx, error):
    if not isinstance(error, commands.CheckFailure): 
      embed=discord.Embed(title="BOT OFICIAL", url="https://gitlab.com/gustavoolrosa2019/bot-pride", description=False, color=0xfe0d0d)
      embed.set_author(name="PRIDE BOT - ERROR", url="https://vignette.wikia.nocookie.net/nanatsu-no-taizai/images/7/7e/Escanor_Anime_Season_3_Design.png/revision/latest/scale-to-width-down/340?cb=20190809211543",icon_url="https://vignette.wikia.nocookie.net/nanatsu-no-taizai/images/7/7e/Escanor_Anime_Season_3_Design.png/revision/latest/scale-to-width-down/340?cb=20190809211543")
      embed.set_thumbnail(url="https://i1.sndcdn.com/artworks-000528753405-uzcj6f-t500x500.jpg")
      embed.add_field(name='ERROR', value='Verifique a sintexe do comando, e tente novamente!',inline=True)
      await ctx.send(embed=embed)


@bot.command()
async def marcar(ctx, user: discord.Member=None):
    if user is None:
        message = ctx.author.mention
@bot.command()
async def slap(ctx, user: discord.Member=None):
    if user is None:
        message = "I don't wanna slap you!"
    else:
        message = "{} was slapped by {}! *ouch*".format(ctx.author.mention,
                                                        user.mention)
    await ctx.send(message)
    

@bot.command()
async def autor(ctx):
    embed = discord.Embed(title='Gustavo de Oliveira Rosa', description="'Somente um sofredor para entender outro sofredor...'- Nagato", color=0xeee657)

    # give info about you here
    embed.add_field(name="Skills", value="HTML\nJavaScript\nCSS\nBOOTSTRAP\nPython\nPHP\nReactNative\nReactJS")

    # give users a link to invite thsi bot to their server
    embed.add_field(name="Idade", value="19 anos")

    await ctx.send(embed=embed)

bot.run(PATH)
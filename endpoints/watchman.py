import discord
from discord.ext import commands
import os
import whois

#Importando variáveis de ambientes globais na aplicacao
from requeriments.vpath import *


#Importando funcoes
from functions.mysql import *


@bot.command()
async def watchman_cadastrar(ctx, nome, dominio, link, tipo, webhook):

    cmdmysql("INSERT into watchman (nome,dominio,link,tipo, usuario, webhook)" + " values ('" + str(nome) + "','" + str(dominio) + "','" + str(link) + "','" + str(tipo) + "', '" + str(ctx.author.mention) + str("','" )+str(webhook)+str("');"))
    embed = discord.Embed(title="Status do comando", description="Adicionado com sucesso!", color=0xeee657)

    await ctx.send(embed=embed)


@bot.command()
async def watchman_listar(ctx):

    name_mysql = cmdmysql("SELECT * from watchman where usuario='" + str(ctx.author.mention)+ "'")

    for row in name_mysql:
        embed = discord.Embed(title=row[1], description=(str("Dominio:")+str(row[2])+str("\n Link:")+str(row[3])+str("\n Tipo:")+str(row[4])), color=0xeee657)
        await ctx.send(embed=embed)

@bot.command()
async def watchman_apagar(ctx,dominio):

    cmdmysql("DELETE FROM watchman where dominio='" + str(dominio)+ "' and usuario='" + str(ctx.author.mention)+ "'")

    embed = discord.Embed(title="Status do comando", description="Dominio removido com sucesso!", color=0xeee657)

    await ctx.send(embed=embed)
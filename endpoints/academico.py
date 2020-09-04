import discord
from discord.ext import commands
import os
import whois

#Importando variáveis de ambientes globais na aplicacao
from requeriments.vpath import *


#Importando funcoes
from functions.mysql import *

@bot.command()
async def trabalhosprontos(ctx):

    name_mysql = cmdmysql("SELECT * from materias")

    for row in name_mysql:
        print("Titulo = ", row[1])
        print("Nome do professor = ", row[2])
        print("Email do professor = ", row[3])
        print('---------------------------------')

        embed = discord.Embed(title=row[1], description=(str("Professor:")+str(row[2])+str("\n Email:")+str(row[3])), color=0xeee657)

        name_mysql2 = cmdmysql(str("SELECT * from gabaritos where materia='")+str(row[1])+str("' and tipo='trabalho'"))

        for row2 in name_mysql2:
            print(row2[1])
            embed.add_field(name=row2[1], value=row2[2])
        await ctx.send(embed=embed)
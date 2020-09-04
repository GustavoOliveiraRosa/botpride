import discord
from discord.ext import commands
import os

from requeriments.vpath import *
from functions.mysql import *
 
@bot.command()
async def root_criar_usuario(ctx,nome,sobrenome,telefone, id_discord, nivel_acesso):
    cmdmysql(str("INSERT INTO usuario (nome,sobrenome,telefone,id_discord, nivel_acesso) values ('")+str(nome)+str("','")+str(sobrenome)+str("','")+str(telefone)+str("','")+str(id_discord)+str("','")+str(nivel_acesso)+str("')"))
    embed=discord.Embed(title="BOT OFICIAL", url="https://gitlab.com/gustavoolrosa2019/bot-pride", description=False, color=0xfe0d0d)
    embed.set_author(name="PRIDE BOT - Registro de usuário", url="https://vignette.wikia.nocookie.net/nanatsu-no-taizai/images/7/7e/Escanor_Anime_Season_3_Design.png/revision/latest/scale-to-width-down/340?cb=20190809211543",icon_url="https://vignette.wikia.nocookie.net/nanatsu-no-taizai/images/7/7e/Escanor_Anime_Season_3_Design.png/revision/latest/scale-to-width-down/340?cb=20190809211543")
    embed.set_thumbnail(url="https://i1.sndcdn.com/artworks-000528753405-uzcj6f-t500x500.jpg")
    confirmacao = (str('Nome: ')+str(nome)+str("\nSobrenome")+str(sobrenome)+str("\nTelefone:")+str(telefone)+str("\n ID DISCORD:")+str(id_discord)+str("\nNivel de Acesso:")+str(nivel_acesso))
    embed.add_field(name='Parábens, usuario cadastrado com sucesso!', value=confirmacao,inline=True)
    await ctx.send(embed=embed)

@bot.command()
async def me_cadastrar(ctx,nome,sobrenome,telefone):
    cmdmysql(str("INSERT INTO usuario (nome,sobrenome,telefone,id_discord) values ('")+str(nome)+str("','")+str(sobrenome)+str("','")+str(telefone)+str("','")+str(ctx.author.mention)+str("')"))
    embed=discord.Embed(title="BOT OFICIAL", url="https://gitlab.com/gustavoolrosa2019/bot-pride", description=False, color=0xfe0d0d)
    embed.set_author(name="PRIDE BOT - Registro de usuário", url="https://vignette.wikia.nocookie.net/nanatsu-no-taizai/images/7/7e/Escanor_Anime_Season_3_Design.png/revision/latest/scale-to-width-down/340?cb=20190809211543",icon_url="https://vignette.wikia.nocookie.net/nanatsu-no-taizai/images/7/7e/Escanor_Anime_Season_3_Design.png/revision/latest/scale-to-width-down/340?cb=20190809211543")
    embed.set_thumbnail(url="https://i1.sndcdn.com/artworks-000528753405-uzcj6f-t500x500.jpg")
    confirmacao = (str('Nome: ')+str(nome)+str("\nSobrenome")+str(sobrenome)+str("\nTelefone:")+str(telefone)+str("\n ID DISCORD:")+str(ctx.author.mention)+str("\nNivel de Acesso:")+str(0))
    embed.add_field(name='Parábens, usuario cadastrado com sucesso!', value=confirmacao,inline=True)
    await ctx.send(embed=embed)

@bot.command()
async def ajuda(ctx):
    categoria = cmdmysql("SELECT * from categoria")
    
    embed=discord.Embed(title="BOT OFICIAL", url="https://gitlab.com/gustavoolrosa2019/bot-pride", description="Não entre em outros links, ou pode ser dar mal, ok? :)", color=0xfe0d0d)
    embed.set_author(name="PRIDE BOT - Comandos", url="https://vignette.wikia.nocookie.net/nanatsu-no-taizai/images/7/7e/Escanor_Anime_Season_3_Design.png/revision/latest/scale-to-width-down/340?cb=20190809211543",icon_url="https://vignette.wikia.nocookie.net/nanatsu-no-taizai/images/7/7e/Escanor_Anime_Season_3_Design.png/revision/latest/scale-to-width-down/340?cb=20190809211543")
    embed.set_thumbnail(url="https://i1.sndcdn.com/artworks-000528753405-uzcj6f-t500x500.jpg")

    for row in categoria:


        comando = cmdmysql(str("SELECT GROUP_CONCAT( comando ORDER BY comando ASC SEPARATOR ',' ) AS todas_categorias FROM comando where categoria='")+str(row[1])+str("'"))
        if comando[0][0] == None:
            comando_filtrado = "Sem comandos"
            embed.add_field(name=row[1], value=str(comando_filtrado),inline=True)
        else:
            embed.add_field(name=row[1], value=str(comando[0][0]),inline=True)
    await ctx.send(embed=embed)

@bot.command()
async def anuncios(ctx):

    name_mysql = cmdmysql("SELECT * from anuncio")
    embed=discord.Embed(title="BOT OFICIAL", url="https://gitlab.com/gustavoolrosa2019/bot-pride", description="Não entre em outros links, ou pode ser dar mal, ok? :)", color=0xfe0d0d)
    embed.set_author(name="PRIDE BOT - Anuncios", url="https://vignette.wikia.nocookie.net/nanatsu-no-taizai/images/7/7e/Escanor_Anime_Season_3_Design.png/revision/latest/scale-to-width-down/340?cb=20190809211543",icon_url="https://vignette.wikia.nocookie.net/nanatsu-no-taizai/images/7/7e/Escanor_Anime_Season_3_Design.png/revision/latest/scale-to-width-down/340?cb=20190809211543")
    embed.set_thumbnail(url="https://i1.sndcdn.com/artworks-000528753405-uzcj6f-t500x500.jpg")
    for row in name_mysql:
        embed.add_field(name=row[1], value=row[2], inline=False)
    await ctx.send(embed=embed)

@bot.command()
async def atualizacoes(ctx):

    name_mysql = cmdmysql("SELECT * from atualizacao")
    embed=discord.Embed(title="BOT OFICIAL", url="https://gitlab.com/gustavoolrosa2019/bot-pride", description="Não entre em outros links, ou pode ser dar mal, ok? :)", color=0xfe0d0d)
    embed.set_author(name="PRIDE BOT - Atualizacoes", url="https://vignette.wikia.nocookie.net/nanatsu-no-taizai/images/7/7e/Escanor_Anime_Season_3_Design.png/revision/latest/scale-to-width-down/340?cb=20190809211543",icon_url="https://vignette.wikia.nocookie.net/nanatsu-no-taizai/images/7/7e/Escanor_Anime_Season_3_Design.png/revision/latest/scale-to-width-down/340?cb=20190809211543")
    embed.set_thumbnail(url="https://i1.sndcdn.com/artworks-000528753405-uzcj6f-t500x500.jpg")
    for row in name_mysql:
        embed.add_field(name=row[1], value=row[2], inline=False)
    await ctx.send(embed=embed)


@bot.command()
async def pride(ctx,pergunta):
    consulta_pergunta = cmdmysql(str("SELECT * from pergunta where pergunta='")+str(pergunta)+str("'"))
    print(consulta_pergunta)
    if consulta_pergunta == ():
        await ctx.send('Não sei te dizer no momento!')
    else:
        await ctx.send(consulta_pergunta[0][2])
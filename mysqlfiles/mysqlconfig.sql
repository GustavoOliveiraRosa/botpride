CREATE DATABASE PRIDE;

USE PRIDE;

CREATE TABLE PRIDE.usuario (
    id_usuario INT (11) NOT NULL AUTO_INCREMENT COMMENT 'ID do usuario',
    nome VARCHAR (255) NOT NULL COMMENT 'Nome',
    sobrenome VARCHAR (255) NOT NULL COMMENT 'Sobrenome',
    telefone VARCHAR (255) NOT NULL COMMENT 'Telefone',
    id_discord VARCHAR (255) NOT NULL COMMENT 'ID Discord',
    nivel_acesso VARCHAR (255) NOT NULL DEFAULT '0',
    PRIMARY KEY (id_usuario)
) CHARSET = utf8;

INSERT INTO usuario (nome,sobrenome,telefone,id_discord,nivel_acesso) values ("gustavo","oliveira","349933340482","123","10000")

CREATE TABLE PRIDE.categoria (
    id_categoria INT (11) NOT NULL AUTO_INCREMENT COMMENT 'ID do usuario',
    nome VARCHAR (255) NOT NULL COMMENT 'Nome',
    descricao VARCHAR (255) NOT NULL COMMENT 'Descricao',
    nivel_acesso VARCHAR (255) NOT NULL DEFAULT '0',
    PRIMARY KEY (id_categoria)
) CHARSET = utf8;

insert into categoria (nome, descricao, nivel_acesso) values ("Essentials", "Comandos essenciais para uso do bot", 0);
insert into categoria (nome, descricao, nivel_acesso) values ("Hacking", "Comandos para hackers :P", 0);
insert into categoria (nome, descricao, nivel_acesso) values ("Watchman", "Comandos para area de monitoramento", 0);
insert into categoria (nome, descricao, nivel_acesso) values ("Academico", "Comandos para area academica", 1);

CREATE TABLE PRIDE.comando (
    id_comando INT (11) NOT NULL AUTO_INCREMENT COMMENT 'ID do usuario',
    categoria VARCHAR (255) NOT NULL COMMENT 'Categoria',
    comando VARCHAR (255) NOT NULL COMMENT 'Comando',
    resposta VARCHAR (255) NOT NULL COMMENT 'Resposta',
    descricao VARCHAR (255) NOT NULL COMMENT 'Descricao',
    nivel_acesso VARCHAR (255) NOT NULL DEFAULT '0',
    PRIMARY KEY (id_comando)
) CHARSET = utf8;

insert into comando (categoria , comando, resposta, descricao, nivel_acesso) values ("Essentials","ola", "ola", "Ola", 0);
insert into comando (categoria , comando, resposta, descricao, nivel_acesso) values ("Hacking","ola", "ola", "Ola", 0);
insert into comando (categoria, comando, resposta, descricao, nivel_acesso) values ("ola", "ola", "Comando ola")

CREATE TABLE PRIDE.anuncio (
    id_anuncio INT (11) NOT NULL AUTO_INCREMENT COMMENT 'ID do anuncio',
    titulo VARCHAR  (255) NOT NULL COMMENT 'Titulo',
    corpo VARCHAR (255) NOT NULL COMMENT 'Corpo',
    PRIMARY KEY (id_anuncio)
) CHARSET = utf8;

insert into anuncio (titulo, corpo) values ("Teste titul", "Testecorpo");
insert into anuncio (titulo, corpo) values ("Teste titul2", "Testecorpo2");

CREATE TABLE PRIDE.atualizacao (
    id_atualizacao INT (11) NOT NULL AUTO_INCREMENT COMMENT 'ID da atualizacao',
    titulo VARCHAR  (255) NOT NULL COMMENT 'Titulo da atualizacao',
    corpo VARCHAR (255) NOT NULL COMMENT 'Descricao',
    data_hora VARCHAR (255) NOT NULL COMMENT 'Data',
    PRIMARY KEY (id_atualizacao)
) CHARSET = utf8;

insert into atualizacao (titulo, corpo, data_hora) values ("Teste titulo 1","teste corpo1", "04:230");
insert into atualizacao (titulo, corpo, data_hora) values ("Teste titulo 2","teste corpo2", "22:22");

CREATE TABLE PRIDE.pergunta (
    id_pergunta INT (11) NOT NULL AUTO_INCREMENT COMMENT 'ID do anuncio',
    pergunta VARCHAR  (255) NOT NULL COMMENT 'Pergunta',
    resposta VARCHAR (255) NOT NULL COMMENT 'Resposta',
    PRIMARY KEY (id_pergunta)
) CHARSET = utf8;

insert into pergunta (pergunta,resposta) values ("ola","ola");

CREATE TABLE PRIDE.gabaritos (
    id_gabarito INT (11) NOT NULL AUTO_INCREMENT COMMENT 'ID do anuncio',
    titulo VARCHAR  (255) NOT NULL COMMENT 'Titulo',
    link_resposta VARCHAR (255) NOT NULL COMMENT 'Link',
    tipo VARCHAR (255) NOT NULL COMMENT 'Tipo',
    materia VARCHAR (255) NOT NULL COMMENT 'Materia',
    PRIMARY KEY (id_gabarito)
) CHARSET = utf8;

CREATE TABLE PRIDE.materias (
    id_materia INT (11) NOT NULL AUTO_INCREMENT COMMENT 'ID do nivel',
    titulo VARCHAR (255) NOT NULL COMMENT 'Titulo do nivel',
    nome_professor VARCHAR (255) NOT NULL COMMENT 'Numero do nivel',
    email_professor VARCHAR (255) NOT NULL COMMENT 'Numero do nivel',
    PRIMARY KEY (id_materia)
) CHARSET = utf8;


CREATE TABLE PRIDE.nivel (
    id_nivel INT (11) NOT NULL AUTO_INCREMENT COMMENT 'ID do nivel',
    titulo VARCHAR (255) NOT NULL COMMENT 'Titulo do nivel',
    numero INT (255) NOT NULL COMMENT 'Numero do nivel',
    PRIMARY KEY (id_nivel)
) CHARSET = utf8;

CREATE TABLE PRIDE.watchman (
        id_aplicacao INT (11) NOT NULL AUTO_INCREMENT COMMENT 'ID do nivel',
        nome VARCHAR (255) NOT NULL COMMENT 'Titulo do nivel',
        dominio VARCHAR (255) NOT NULL COMMENT 'Numero do nivel',
        link VARCHAR (255) NOT NULL COMMENT 'Link',
        tipo VARCHAR (255) NOT NULL COMMENT 'Tipo',
        usuario VARCHAR (255) NOT NULL COMMENT 'Usuario',
        webhook VARCHAR (255) NOT NULL COMMENT 'webhook',
        PRIMARY KEY (id_aplicacao)
    ) CHARSET = utf8;
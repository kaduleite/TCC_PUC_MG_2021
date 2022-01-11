#!/usr/bin/env python
# coding: utf-8

# # Classificação dos modelos de motocicleta a partir da descrição do produto

import pandas as pd, numpy as np
import re

# ### Importa as stopwords da língua portuguesa
# Importar lista de Stopwords
from nltk.corpus import stopwords
stopwords = set(stopwords.words('portuguese'))
# Palavras a adicionar na lista de stopwords estão contidas em um arquivo csv externo
dfsw = pd.read_csv('./bases/stopwords.csv', encoding='ISO-8859-1')
stopwords_df=sorted(list(dfsw['stopword']))
# Atualizar stopwords
stopwords.update(stopwords_df)

# ### Carrega lista de aplicações e cria palavrasChave
# carrega a lista de marcas de motos do arquivo
dftemp=pd.read_csv('./bases/Aplicacoes.csv')
# remove caracteres especiais ou soltos e termos duplicados, salvando na lista
palavrasChave=sorted(set(re.sub(r"\b \w \b",
                                ' ', 
                                re.sub(r"[/<>()|\+\$%&#@\'\"]+", 
                                       " ",
                                       " ".join(dftemp['APLICACOES'].tolist()))).split()))

# #### Função de limpeza de dados irrelevantes para a classificação e remoção de stopwords
def limpaDescricao(descricao): # 
    descricao=descricao.lower() #transformar em minúsculas
    descricao=re.sub(r"\( *\d*[/\*\-\d]\d* *\)", ' ', descricao) # remove códigos numéricos entre parênteses com -*/
    # remove a ocorrência de "código e etc." e o termo seguinte começado com número
    # att: (alguns tem hífen ou asterisco) (colocar antes de remover pontuação)
    descricao=re.sub(r"\b(invoice|código|codigo|cod|cód|(certificado|cert)( no|nr|)|ref)[0-9a-z/\-\*\.\:]* *\d[^ ]+", ' ', descricao)
    # remove identificação de referência de engrenagens dos kits (antes da pontuação)
    descricao=re.sub(r"\d{1,}(ho|uo|h|l|z|t|ktd|m|d| dentes) *([^\s]+)|\w*(ho|h|l|z|t|ktd|m|d| dentes)\d{1,}([^\s]+)", ' ', descricao) # 00h
    # remove códigos no início da descrição
    descricao=re.sub(r"^\b\d{2,}[^ ]*\b", ' ', descricao)    
    descricao=re.sub(r"- | -|[\\\+,.:;!?/]+", ' ', descricao) #remover pontuação (att: "- " ou " -")
    descricao=re.sub(r"[/<>()|\+\\$%&#@\'\"]+", ' ', descricao) #remover carcteres especiais
    # substituição de termos comuns
    termos=[('pop100', 'pop 100'),('c 100', 'c100'),('titan150','titan 150'),('tit','titan')]
    for termo in termos:
        descricao=re.sub(r"\b" + str(termo[0]) + r"\b", termo[1], descricao)
    # remove a ocorrência de medidas tipo 00x000x00 ou 000x0000
    descricao=re.sub(r"\b\d{1,}(x|\*)\d{1,}(x|\*)\d{1,}|\d{1,}(x|\*)\d{1,}\b", ' ', descricao)
    # remove identificação de quantidades, unidades, peças e conjuntos
    descricao=re.sub(r"\b(\d* *(conj|und|uni|pc|pç|pec|peç)( \w|\w)+?)\b", ' ', descricao)
    # remove identificação de mais de 4 dígitos com ou sem letras no início e no final
    descricao=re.sub(r"\w+\d{4,}\w+", ' ', descricao)
    # remove números de 4 dígitos ou mais começados de 2 a 9
    descricao=re.sub(r"\b[02-9]\d{3,}\b", ' ', descricao)
    # remove identificação de termos começados por zero
    descricao=re.sub(r"\b0\d*\w+?(?=\b)", ' ', descricao)
    # remove a ocorrência de "marca " e o termo na lista até o próximo espaço
    for marca in ['kmc gold','king']: descricao=re.sub(r"\bmarca *"+str(marca)+r"[^ ]*", ' ', descricao) # colocar antes das stopwords
    # remove stopwords mantendo a ordem original da descrição
    descricao=list(dict.fromkeys(descricao.split())) # cria lista com termos únicos
    descricao=" ".join([x for x in descricao if x not in set(stopwords)]) # exclui stopwords
    # limpa os número que não estão na lista de aplicações (colocar depois das stopwords)
    desc=descricao.upper().split() # quebra a descrição
    dif=list(set(descricao.upper().split()).difference(palavrasChave)) # pega os termos diferentes de palavrasChave
    [desc.remove(x) for x in desc if (x in dif and x.isnumeric())] # exclui de desc os termos numéricos diferentes
    descricao=" ".join(desc).lower() # volta para texto
    #remover hífen, letras ou números soltos (deixar duplicado mesmo)
    descricao=re.sub(r"(^-| -|- |\b\w\b)", ' ', descricao)
    descricao=re.sub(r"(^-| -|- |\b\w\b)", ' ', descricao)
    #substitui remove o i das cilindradas: ex.: 125i por 125
    termos=re.findall(r"\d*i\b",descricao)
    if termos:
        for termo in termos:descricao=descricao.replace(termo,termo[:-1])
    # remove espaços em excesso (colocar no final)
    descricao=re.sub(r" {2,}", ' ', descricao)
    descricao=descricao.strip()
    # retorna a descricao como saída da função
    return descricao # retorna a descrição

# #### Função de determinação de palavras chave na coluna Modelo
def achaPalavraChave(descricao):
    palavras=[]
    descricao=descricao.upper()
    desc=descricao.split()
    for palavra in palavrasChave:
        if palavra in desc:
            palavras.append(palavra)
        else:
            if len(palavra)>=3 and not palavra.isnumeric():
                if palavra in ["CROSS","STAR","NIX"]: # termos que só interessam no início
                    pat=r"\b"+str(palavra)+r"\d*\b" # termo iniciando pela palavra seguido de dígitos
                else:
                    pat=r""+str(palavra)+r"\w*(?=\b|\d*\b)" # termo iniciando ou terminando pela palavra seguido de números
            else:
                pat=r"\b"+str(palavra)+r"\b" # termo completo
            a = re.search(pat,descricao)
            if a:
                palavras.append(palavra)
                paltemp=a.group(0)[len(palavra):] # parte que sobra de palavra
                if paltemp in palavrasChave: # se a parte também estiver em palavrasChave
                    palavras.append(paltemp) # adiciona parte também
    palavras=list(set(palavras)) # remove duplicados
    palavras=" ".join(palavras) # converte para string
    return palavras

# #### Função para acrescentar a marca da motocicleta
# termos que iniciam item da descrição correspondem a marca
Marcas = {'HONDA': ['CG','CB','CRF','BIZ','BROS','XL','FAN','XR','XRE'
                    'TITAN','TODAY','TWIN','POP','NX','NXR'],
          'YAMAHA': ['DT','FZ','FJ','RD','MT','XF','XJ','XS','XT','XZ','YF','LANDER',
                     'YBR','YZ','VIRAGO','FACTOR','EC','CRYPTON','FAZER'],
          'ZONGSHEN': ['ZS'],
          'KASINSKI': ['COMET'],
          'POLARIS': ['SPORTSMAN','RZR','RANGER'],
          'KAWASAKI': ['NINJA','GTR','KDX','KL','KX','KZ','ZR','ZZ','ER6N','ER6F'],
          'DAYANG': ['DY1','DY2','DY5']}

# Função para pegar a chave pelo valor, dado que valor é único.
def pegaChave(v, dict):
    for chave, valores in dict.items():
        if type(valores)!=type([1,2]):
            valores=[valores]
        for valor in valores:
            if v == valor:
                return chave
    return "Não existe chave para esse valor."

def acrescentaMarca(descricao):
    desclst=descricao.upper().split()
    for termo in desclst:
        if termo in Marcas:
            return descricao
    for marca in Marcas:
        for termo in Marcas[marca]:
            pat=r"\b"+ termo +"\b*"
            if re.search(pat,descricao.upper()):
                return pegaChave(termo,Marcas).upper() + " " + descricao.upper()
    return descricao

# ### Função final que transforma a DESCRICAO DO PRODUTO em Modelo para classificar
def criaModelo(descricao):
    descricao=limpaDescricao(descricao)
    descricao=achaPalavraChave(descricao)
    descricao=acrescentaMarca(descricao)
    return descricao

# ### Função que determina a existência de retentor no kit e retorna True|False
def retentorAux(descricao):
    # define o padrão de busca
    padrao = r'c/ *ret|com *ret' #r"(com|c/) *ret"
    descricao=descricao.lower()
    busca = re.findall(padrao, descricao)
    if busca:
        descricao = busca[0]
        return True
    else:
        descricao=''
        return False
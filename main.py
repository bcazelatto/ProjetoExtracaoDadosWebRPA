from log import Logging
from settings import configTelegram
from abrirChrome import Chrome
from extrairDadosWeb import ExtrairInformacao
from addDadosExcel import Excel
from sendEmail import Email

# coding=utf-8
try:
    Logging.execute(configTelegram.status, 'INFO', 'INICIANDO PROJETO PESSOAL RPA')

    # Executar Chrome
    # PS. Para esse bot não é necessário nem abrir o chrome para extrair os dados
    #if not Chrome.execute():
    #    raise Exception('NAO FOI POSSIVEL ABRIR O CHROME')

    # Extrai dados
    dados = ExtrairInformacao.execute()
    if dados is None:
        raise Exception('NAO FOI POSSIVEL EXTRAIR TABELA')
    
    # Adiciona dados em um Excel
    if not Excel.criarExcel(dados):
        raise Exception('NAO FOI POSSIVEL ADICIONAR DADOS EM UM ARQUIVO EXCEL')
    
    #Enviar dados por email
    if not Email.send():
        raise Exception('NAO FOI POSSIVEL ENVIAR EMAIL')

    Logging.execute(configTelegram.status, 'INFO', 'FIM DA EXECUCAO DO PROJETO PESSOAL RPA')
except Exception as e:
    Logging.execute(configTelegram.status, 'ERROR', f'NAO FOI POSSIVEL EXECUTAR PROJETO PESSOAL RPA - {e}')




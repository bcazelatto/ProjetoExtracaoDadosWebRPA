import os

class ConfigLog:
    # Diretório atual
    diretorio_padrao = os.environ['USERPROFILE']

    # Configs LOG
    caminho_log = f"{diretorio_padrao}/eclipse-workspace/Python/RPA/ProjetoPessoal_RPA/Log"

class configEmail:
    # Configs EMAIL
    host = "smtp.office365.com"
    port = 587
    username = "brunocazelatto@sis-it.com"
    password = "LT$Hohyq"
    to = "bcazelatto@gmail.com"

class configChrome:
    # Caminho do Chrome
    url = "https://www.todamateria.com.br/estados-do-brasil/"

class configExcel:
    # Diretório atual
    diretorio_padrao = os.environ['USERPROFILE']

    caminho_saida_excel = f'{diretorio_padrao}\eclipse-workspace\Python\RPA\ProjetoPessoal_RPA\SaidaArquivo'
    nome_arquivo = 'dados_da_tabela'
    extensao_arquivo = 'xlsx'

class configTelegram:
    # Habilitar telegram
    status = False
    # Token do seu bot no Telegram
    token = '7012757416:AAHkJbmLEtCDd0ERpub_YFWWj3zZSMi_mjM'
    # ID do chat onde a mensagem será enviada
    chat_id = '-4193820155'

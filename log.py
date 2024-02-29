import os
from settings import ConfigLog, configTelegram
from datetime import datetime
import telegram

class Logging:
    def execute(habilitaTelegram, status, mensagem):
        # Obtendo a data e hora atual
        data_hora_atual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        data_atual = datetime.now().strftime("%Y%m%d")

        if habilitaTelegram:
           telegram.send_message(configTelegram.token, configTelegram.chat_id, f'{data_hora_atual}: {status} - {mensagem}') 

        if not os.path.exists(ConfigLog.caminho_log):
            os.makedirs(ConfigLog.caminho_log)
        
        caminho_arquivo_log = os.path.join(ConfigLog.caminho_log, f'{data_atual}_LOGTECNICO.txt')

        with open (caminho_arquivo_log, 'a') as arquivo:
            #Escrevendo log
            arquivo.write(f'{data_hora_atual}: {status} - {mensagem}\n')


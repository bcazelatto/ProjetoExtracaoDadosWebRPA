import requests
import pandas as pd
from settings import configChrome, configTelegram
from log import Logging
from bs4 import  BeautifulSoup

class ExtrairInformacao:

    def execute():
        Logging.execute(configTelegram.status, 'INFO', f'INICIANDO EXTRACAO DE INFORMACOES DO SITE [{configChrome.url}]'.upper())
        try:
            req = requests.get(configChrome.url)

            if req.status_code == 200:
                content = req.content
                soup = BeautifulSoup(content, 'html.parser')
                tabela = soup.find(name='table')
                dataFrame = pd.read_html(str(tabela))[0]
                return dataFrame

        except Exception as e:
            Logging.execute(configTelegram.status, 'ERROR', f'NAO FOI POSSIVEL EXTRAIR INFORMACAO DO SITE [{configChrome.url}]'.upper())
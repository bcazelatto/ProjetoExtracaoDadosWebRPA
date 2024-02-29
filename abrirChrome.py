from settings import configTelegram
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from settings import configChrome
from log import Logging

class Chrome:

    def execute():
        try:
            Logging.execute(configTelegram.status, 'INFO', 'INICIANDO ABERTURA DO CHROME')
            
            # Configurar as opções do Chrome
            chrome_options = Options()
            chrome_options.add_argument('--start-maximized')
            chrome_options.add_argument('--ignore-certificate-errors')
            chrome_options.add_argument('--ignore-ssl-errors')
            
            # Inicializar o driver do Chrome com as opções configuradas
            driver = webdriver.Chrome(options=chrome_options)


            # Abrir uma URL
            driver.get(configChrome.url)

            Logging.execute(configTelegram.status, 'INFO', 'CHROME ABERTO COM SUCESSO')
            return True
        except Exception as e:
            Logging.execute(configTelegram.status, 'ERROR', f'NÃO FOI POSSÍVEL ABRIR O CHROME - {e}')
            return False
        
import os
from log import Logging
from settings import configExcel, configTelegram

class Excel:

    def criarExcel(dados):
        try:
            Logging.execute(configTelegram.status, 'INFO', 'INICIANDO CRIACAO ARQUIVO EXCEL')

            if not os.path.exists(configExcel.caminho_saida_excel):
                os.makedirs(configExcel.caminho_saida_excel)
                Logging.execute(configTelegram.status, 'INFO', 'CRIADO PASTA DE SAIDA PARA O ARQUIVO EXCEL')

            # Salvar o DataFrame em um arquivo Excel
            dados.to_excel(f'{configExcel.caminho_saida_excel}\dados_da_tabela.xlsx', index=False)
            Logging.execute(configTelegram.status, 'INFO', 'ARQUIVO EXCEL CRIADO COM SUCESSO')
            return True
            
        except Exception as e:
            Logging.execute(configTelegram.status, 'ERROR', f'ERRO ANO CRIAR O ARQUIVO EXCEL - {e}')
            return False

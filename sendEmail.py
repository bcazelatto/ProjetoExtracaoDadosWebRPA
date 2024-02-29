import smtplib
import pandas as pd
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from log import Logging
from settings import configEmail, configExcel, configTelegram

class Email:

    def send():
        Logging.execute(configTelegram.status, 'INFO', 'INICIANDO ENVIO DO EMAIL')
        try:
            # Ler informacoes do excel
            tabela_vendas = pd.read_excel(f'{configExcel.caminho_saida_excel}/{configExcel.nome_arquivo}.{configExcel.extensao_arquivo}')
            mail_body = f'''
            <html>
            <head></head>
            <body>
                <p>Prezados,</P>

                <p>Segue o relatório dos Estados do Brasil.</P>

                <p><strong>Tabela Dos Estados:</strong></P>
                {tabela_vendas.to_html()}

                <p>Qualquer dúvida estou a disposição.</P>

                <p>Atenciosamente.</P>
            </body>
            </html>
            '''

            mimemsg = MIMEMultipart()
            mimemsg['From'] = configEmail.username
            mimemsg['To'] = configEmail.to
            mimemsg['Subject'] = 'Relatório de Estados do Estados, Siglas e Capitais do Brasil!'
            mimemsg.attach(MIMEText(mail_body, 'html'))

            connection = smtplib.SMTP(configEmail.host, configEmail.port)
            connection.starttls()
            connection.login(configEmail.username, configEmail.password)
            connection.send_message(mimemsg)
            connection.quit()
            Logging.execute(configTelegram.status, 'INFO', 'FINALIZADO ENVIO DO EMAIL COM SUCESSO')
            return True
        except Exception as e:
            Logging.execute(configTelegram.status, 'ERROR', f'NAO FOI POSSIVEL ENVIAR O EMAIL - {e}')
            return False
            
from string import Template
from datetime import datetime
from dados_aleatorios import meu_email, senha, email_cliente

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib

with open(r'String - Template\templates.html', 'r') as html:
    template = Template(html.read())
    data_atual = datetime.now().strftime('%d/%m/%Y')
    corpo_msg = template.substitute(nome='Theo', data=data_atual)

msg = MIMEMultipart()
msg['from'] = 'Sr.sexo'
msg['to'] = meu_email
msg['subject'] = 'Corra'

corpo = MIMEText(corpo_msg, 'html')
msg.attach(corpo)

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(meu_email, senha)
    smtp.send_message(msg)
    print("Email enviado com sucesso")

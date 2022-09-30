"""
Comma Separated Values - CSV 
É um formato de dados muitos usados em tabelas (Excel, Google Sheets), bases de dados,
clientes de e-mail, etc...
"""
import csv

with open('D:\Projeto.py\Modulo 05\Comma Separated Values - CSV\clientes.csv', 'r') as arquivo:
    dados = csv.reader(arquivo)

    for dado in dados:
        print(dado["Nome"])

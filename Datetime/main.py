from datetime import datetime, timedelta

# .strptime(str, fmt) -> recebe em string e transforma em um horario valido
# .strftime(fmt) -> vc cria um datetime seguindo as ordens de:
#       Ano, Mes, Dia, Hora, Minutok, logo apos se deve fazer isso:
#       ('%d/%m/%Y %H:%M:%S')) <- Formatação por dia, mes, ano, hora, minuto, segundo
#


# data = datetime(2022, 9, 22, 16, 18)
# print(data.strftime('%d/%m/%Y %H:%M:%S'))

data = datetime.strptime('22/09/2022', '%d/%m/%Y')
print(data.timestamp())

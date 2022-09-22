from datetime import datetime, timedelta

# .strptime(str, fmt) -> recebe em string e transforma em um horario valido

# .strftime(fmt) -> vc cria um datetime seguindo as ordens de:
#       Ano, Mes, Dia, Hora, Minutok, logo apos se deve fazer isso:
#       ('%d/%m/%Y %H:%M:%S')) <- Formatação por dia, mes, ano, hora, minuto, segundo
#
# .timestamp() -> A timestamp is encoded information generally used in UNIX, which indicates the date and time at which a particular event has occurred.
# This information could be accurate to the microseconds.
# It is a POSIX timestamp corresponding to the datetime instance.
#


# data = datetime(2022, 9, 22, 16, 18)
# print(data.strftime('%d/%m/%Y %H:%M:%S'))

d1 = datetime.strptime('20/04/1987 20:00:00', '%d/%m/%Y %H:%M:S')
d2 = datetime.strptime('27/07/2004 23:31:09', '%d/%m/%Y %H:%M:S')
dif = d1 - d2
print(dif)

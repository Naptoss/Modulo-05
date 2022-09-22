from datetime import datetime
from locale import setlocale, LC_ALL

setlocale(LC_ALL, '')

dt = datetime.now()
formatacao = dt.strftime('%A, %d de %B de Y%')
print(formatacao)

from datetime import datetime, timedelta

# data = datetime(2022, 9, 22, 16, 18)
# print(data.strftime('%d/%m/%Y %H:%M:%S'))

data = datetime.strptime('22/09/2022', '%d/%m/%Y')
print(data.timestamp())


from datetime import datetime, timedelta

data = datetime.strptime('08/11/1948 20:00:00', '%d/%m/%Y %H:%M:%S')
data = data + timedelta(days=5, seconds=2*60*60)
print(data.strftime('%d/%m/%Y %H:%M:%S'))

d1 = datetime.strptime('08/11/1948 20:00:00', '%d/%m/%Y %H:%M:%S')
d2 = datetime.strptime('04/10/1949 10:00:00', '%d/%m/%Y %H:%M:%S')

dif = d2 - d1
print(dif)

import datetime

c = datetime.datetime(2021, 6, 21, 3, 14, 59)
x = datetime.datetime.now().replace(microsecond=0)

print((x - c).total_seconds())
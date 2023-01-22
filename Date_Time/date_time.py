from datetime import datetime
import pytz

dt = datetime.now()
# print(dt)
# print(dt.day)
# print(dt.month)
# print(dt.year)
# print(dt.hour)
# print(dt.minute)
# print(dt.second)
# print(dt.weekday())
# print(dt.isoweekday())
tz = pytz.timezone("Asia/Kolkata")
print(tz)
dt_tz = tz.localize(dt)
print(dt_tz)

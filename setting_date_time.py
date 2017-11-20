import datetime
import random
import pytz
import time


today = datetime.datetime.today().astimezone(tz=pytz.timezone('Asia/Kolkata'))
delta = datetime.timedelta(days=1)
tomorrow = today + delta

list_ = ['4 30 0','4 15 0','4 5 0','4 45 0','5 0 0','5 15 0','5 30 0','5 20 0','5 25 0']
good_morning_time = random.choice(list_)
wish_time = datetime.datetime.strptime(good_morning_time,'%H %M %S')

wish_datetime = datetime.datetime(tomorrow.year,tomorrow.month,tomorrow.day,wish_time.hour,wish_time.minute,wish_time.second)
wish_datetime = pytz.timezone('Asia/Kolkata').localize(wish_datetime)
print('Wishing at {}'.format(wish_datetime))


today = datetime.datetime.now().astimezone(tz=pytz.timezone('Asia/Kolkata'))
print('Current date-time : {}'.format(today))

sleep_time = (wish_datetime - today)
print(sleep_time.total_seconds())

time.sleep(sleep_time.total_seconds())
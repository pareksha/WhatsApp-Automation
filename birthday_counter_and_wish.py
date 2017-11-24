import random
import pytz
import sys
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import datetime
import time

driver = webdriver.Chrome('/home/pareksha/PycharmProjects/learning_python/drivers/chromedriver')
driver.get('https://web.whatsapp.com/')

try:
    WebDriverWait(driver,20).until(EC.presence_of_element_located((By.CLASS_NAME,'input-search')))
except Exception as e:
    print('Login Failed')
    sys.exit(0)

print('Logged in')

current_dt = datetime.datetime.today().astimezone(tz=pytz.timezone('Asia/Kolkata'))
print('Current time :',current_dt.time())

bday_dt = datetime.datetime(2017,11,25,0,0,0)
bday_dt = pytz.timezone('Asia/Kolkata').localize(bday_dt)

print('Wishing time :',bday_dt.time())

remaining_time = bday_dt - current_dt
print('Remaining time :',remaining_time)

seconds_remaining = remaining_time.total_seconds()
print('Seconds remaining : ',seconds_remaining)

wish_start_dt = datetime.datetime(2017,11,24,23,30,0)
wish_start_dt = pytz.timezone('Asia/Kolkata').localize(wish_start_dt)
print('Wishing starts at ',wish_start_dt.time())

list_ = ['sweety','jaan','cat vaali bachi','behna','half girlfriend','bass aane vaala hai','maate','hone vaali b\'day girl','b\'day girl']

minutes_to_go = (bday_dt - wish_start_dt).total_seconds()
minutes_to_go = minutes_to_go/60
print('Program resumes in',minutes_to_go)

time.sleep((wish_start_dt - current_dt).total_seconds())

actions = ActionChains(driver)
actions.send_keys(Keys.TAB)
actions.send_keys('Shreya')
actions.send_keys(Keys.RETURN)
actions.perform()
time.sleep(1)

while(1):
    if seconds_remaining <= 0:
        actions = ActionChains(driver)
        actions.send_keys('Happy Birthday.... !!!!')
        actions.send_keys(Keys.RETURN)
        actions.perform()
        time.sleep(1)
        break

    elif minutes_to_go <= 1:
        actions = ActionChains(driver)
        seconds_remaining = (bday_dt - datetime.datetime.today().astimezone(tz=pytz.timezone('Asia/Kolkata'))).total_seconds()
        seconds_remaining = int(seconds_remaining)
        actions.send_keys('{} seconds...'.format(seconds_remaining))
        actions.send_keys(Keys.RETURN)
        time.sleep(2)
        actions.perform()

    else:
        actions = ActionChains(driver)
        actions.send_keys('{} minutes to go.. '.format(minutes_to_go),random.choice(list_) , '...!!!')
        actions.send_keys(Keys.RETURN)
        actions.perform()
        time.sleep(1)
        minutes_to_go -= 1
        time.sleep(60)

actions = ActionChains(driver)
actions.send_keys('Dhanyavaad kal boliyo... i sone jaa riii.. tata.. gunyt.. !!')
actions.send_keys(Keys.RETURN)
actions.perform()
driver.quit()
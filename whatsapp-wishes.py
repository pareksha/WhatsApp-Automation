import datetime
import pytz
import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Firefox(executable_path='/home/pareksha/PycharmProjects/learning_python/drivers/geckodriver')
driver.get('https://web.whatsapp.com/')

try:
    login = WebDriverWait(driver,60).until(EC.presence_of_element_located((By.CLASS_NAME,'input-search')))
except:
    print('Unable to log in')

actions = ActionChains(driver)
actions.send_keys(Keys.TAB)
actions.send_keys('Gourav')
actions.send_keys(Keys.RETURN)
actions.perform()

smilies = ['kiss','hug','smile','blush','ghost','cool','smiling','clown']
text_1 = ['Good Morning Bhiiiiyyyaaaa..... !!!!','Very good morning..!!!!','Uth jao bhaiya.. subeh ho gayi..!!!!'
    ,'Namaste bhiiiiiyyyaaa..!!!!','Gooodddiieee morning melle pyaare bhiiyyyaaaa...!!!!','Morning ho gayii bhaiya..!!!!']
text_2 = ['Have a good day bhaiya..','Have a nice and beautiful day my sweetu bhaiya... ',
          'Aapka dinn sukhi avam mangalmay ho..','Love you bhiiiyyaaaa..','Good day.. melle pyaare bhaiya']

while(1):
    today = datetime.datetime.today().astimezone(tz=pytz.timezone('Asia/Kolkata'))
    delta = datetime.timedelta(days=1)
    tomorrow = today + delta

    list_ = ['4 30 0', '4 15 0', '4 5 0', '4 45 0', '5 0 0', '5 15 0', '5 30 0', '5 20 0', '5 25 0']
    good_morning_time = random.choice(list_)
    wish_time = datetime.datetime.strptime(good_morning_time, '%H %M %S')

    wish_datetime = datetime.datetime(tomorrow.year, tomorrow.month, tomorrow.day, wish_time.hour, wish_time.minute,
                                      wish_time.second)
    wish_datetime = pytz.timezone('Asia/Kolkata').localize(wish_datetime)
    print('Wishing at {}'.format(wish_datetime))

    today = datetime.datetime.now().astimezone(tz=pytz.timezone('Asia/Kolkata'))
    print('Current date-time : {}'.format(today))

    sleep_time = (wish_datetime - today)
    print(sleep_time.total_seconds())

    time.sleep(sleep_time.total_seconds())


    actions = ActionChains(driver)
    actions.send_keys(Keys.TAB)
    actions.send_keys('Notepad')
    actions.send_keys(Keys.ENTER)
    actions.perform()

    time.sleep(2)

    actions = ActionChains(driver)
    actions.send_keys(random.choice(text_1))
    actions.send_keys(Keys.ENTER)
    actions.perform()

    time.sleep(2)

    actions = ActionChains(driver)
    actions.send_keys(random.choice(text_2))
    for x in range(3):
        actions.send_keys(Keys.TAB)
    actions.send_keys(Keys.RETURN)
    actions.perform()

    time.sleep(2)

    actions = ActionChains(driver)
    actions.send_keys(random.choice(smilies))
    for y in range(2):
        actions.send_keys(Keys.RETURN)
    actions.perform()

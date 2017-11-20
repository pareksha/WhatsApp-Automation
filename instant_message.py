from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
import random

driver = webdriver.Firefox(executable_path='/home/pareksha/PycharmProjects/learning_python/drivers/geckodriver')
driver.get('https://web.whatsapp.com/')

try:
    WebDriverWait(driver,30).until(EC.presence_of_element_located((By.CLASS_NAME,'input-search')))
except:
    print('Login Failed')


smilies = ['kiss','hug','smile','blush','ghost','cool','smiling','clown']
text_1 = ['Good Morning Bhiiiiyyyaaaa..... !!!!','Very good morning..!!!!','Uth jao bhaiya.. subeh ho gayi..!!!!'
    ,'Namaste bhiiiiiyyyaaa..!!!!','Gooodddiieee morning melle pyaare bhiiyyyaaaa...!!!!','Morning ho gayii bhaiya..!!!!']
text_2 = ['Have a good day bhaiya..','Have a nice and beautiful day my sweetu bhaiya... ',
          'Aapka dinn sukhi avam mangalmay ho..','Love you bhiiiyyaaaa..','Good day.. melle pyaare bhaiya']


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

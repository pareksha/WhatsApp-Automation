import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome(executable_path='/home/pareksha/PycharmProjects/learning_python/drivers/chromedriver')
driver.get('https://web.whatsapp.com/')

try:
    WebDriverWait(driver,30).until(EC.presence_of_element_located((By.CLASS_NAME,'input-search')))
    print('Login Successful')
except Exception as e:
    print(e)
    print('Login Failed')

actions = ActionChains(driver)
actions.send_keys(Keys.TAB)
actions.send_keys('Notepad')
actions.send_keys(Keys.RETURN)
actions.perform()

time.sleep(2)

string = '''
                     X
                X       X
            X               X
        X       HAPPY     X
    X       BIRTHDAY     X
 X            NIKHIL           X
     X        BHAIYA       X
         X                     X
             X             X
                 X     X
                     X
'''

actions = ActionChains(driver)
actions.send_keys('To bhaiya-')


for char in string:
    if char == 'X':
        emoji_container = driver.find_element_by_class_name('compose-btn-emoji').click()
        actions = ActionChains(driver)
        actions.send_keys('cake')
        actions.send_keys(Keys.RETURN)
        actions.perform()
        emoji_container = driver.find_element_by_class_name('emoji-button-container')
        emoji_container.click()
        time.sleep(1)

    elif char == '\n':
        actions = ActionChains(driver)
        actions.key_down(Keys.SHIFT).send_keys(Keys.ENTER).key_up(Keys.SHIFT)
        actions.perform()


    else:
        actions = ActionChains(driver)
        actions.send_keys(char)
        actions.perform()

actions = ActionChains(driver)
actions.send_keys(Keys.ENTER)
driver.quit()

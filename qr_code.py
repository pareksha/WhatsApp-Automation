import time
from selenium import webdriver

driver = webdriver.Chrome(executable_path='/home/pareksha/PycharmProjects/learning_python/drivers/chromedriver')
driver.get('https://web.whatsapp.com/')

time.sleep(3)
screenshot = driver.save_screenshot('qr_code.png')
print('Screenshot Captured')
open(screenshot)
time.sleep(5)

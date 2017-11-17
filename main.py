#Simple code to get started with selenium

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("/home/pareksha/PycharmProjects/learning_python/drivers/chromedriver")
driver.get("http://google.com")

search_bar = driver.find_element_by_name("q")
search_bar.clear()

search_bar.send_keys("Health is Wealth")
search_bar.send_keys(Keys.ENTER)

driver.close()
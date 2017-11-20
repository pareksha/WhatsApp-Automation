from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random

driver = webdriver.Chrome("/home/pareksha/PycharmProjects/learning_python/drivers/chromedriver")
driver.get("https://web.whatsapp.com/")

# list_ = ["Prateek padh le","Online mat beth","Assignment bana le","Attendance puuri kar le","Physics padh lii?","Nahii padhii toh padh le","Minors aa rahe hai","Ratein jaagg","Puuri raat padhhiiyo","padh padh padh","Number laa","Mummy papa ko khush kar"]
# list_ = ["I love you","Melllee pyaarrreee bhiiyyaaa","Shone bhiiiiyyyyaaaa","None bhiiiiiyyyyyyaaaaa","Pyaare pyaare bhiiiyyaaaa","Bhiiyyaaa speech bana lo","All the best bhiiyyaaaa"]
# list_ = ["Namaste","Kya haal","AAjjjaaaa","CAT aane vaala hai","Half boyfriend kaisa hai","Namasttteeeeeeeee","Pyaaaarrrriiiii behna kidddaannn"]
# list_ = ["All the best for minors","Study hard.. get good marks","Best of luck","My good wishes are with you","Saari raat padhna","Enjoy study time"]

time.sleep(15)
search_bar = driver.find_element_by_class_name("input-search")
search_bar.send_keys("deepinder")
search_bar.send_keys(Keys.ENTER)

for x in range(50):
    msg_box = driver.find_element_by_class_name("pluggable-input-body")
    msg_box.send_keys("All the best for exams bro...!!!")
    msg_box.send_keys(Keys.ENTER)

driver.close()

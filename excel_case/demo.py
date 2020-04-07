import random
from time import sleep
from selenium import webdriver

list = []
while True:
    a = random.randint(1,51)
    list.append(a)
    sleep(1)
    #print(a)
    print(list)

# driver = webdriver.Chrome()
# driver.get('https://www.baidu.com')
# driver.maximize_window()
# sleep(2)
# driver.close()

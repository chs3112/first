import selenium
from selenium import webdriver
from selenium.webdriver import ActionChains

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait

import time

URL = 'https://forms.gle/UwwaHMgaffDaj2wD9'

driver = webdriver.Chrome(executable_path='chromedriver')
driver.get(url=URL)

while 1:
    driver.implicitly_wait(5)

    a = ["i5",'i15','i28','i41','i49','i80','i93','i138','i152','i155','i158','i161','i164','i167','i170','i173','i176',
        'i179','i186','i200','i211','i214','i217','i220','i237']

    for i in a:
        q = driver.find_element_by_id(i)
        q.click()
        
    q = driver.find_elements_by_xpath("//*[@class='freebirdFormviewerComponentsQuestionTextRoot']/div/div/div/textarea")
    q[0].send_keys("데이트 폭력이 심각해서")
    q[1].send_keys("데이트를 더 잘하게 되었다")
    q[2].send_keys("어차피 연애를 못한다")

    an = driver.find_element_by_xpath('//*[@class="freebirdFormviewerViewNavigationLeftButtons"]/div')
    an.click()
    driver.implicitly_wait(5)

    b = driver.find_element_by_xpath('//*[@class="freebirdFormviewerViewResponseLinksContainer"]/a')
    b.click()
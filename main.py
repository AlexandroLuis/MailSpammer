'''
Chromedriver: https://chromedriver.storage.googleapis.com/index.html
'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import pyautogui

driver = webdriver.Chrome(executable_path="C:/LOCATION/chromedriver")

driver.get("https://stackoverflow.com/users/signup?ssrc=head&returnurl=%2Fusers%2Fstory%2Fcurrent%27")
sleep(3)
driver.find_element_by_xpath('//*[@id="openid-buttons"]/button[1]').click()

driver.find_element_by_xpath('//input[@type="email"]').send_keys("SENDERMAIL")
driver.find_element_by_xpath('//*[@id="identifierNext"]').click()

sleep(3)
driver.find_element_by_xpath('//input[@type="password"]').send_keys("SENDERPASS")
pyautogui.press('enter')
sleep(3)

driver.get("https://mail.google.com")
sleep(5)

for i in range(3):
    driver.get("https://mail.google.com/mail/u/0/#inbox?compose=new")
    sleep(10)
    driver.find_element_by_class_name("vO").send_keys("RECEIVER")
    driver.find_element_by_class_name("aoT").send_keys("SUBJECT")
    driver.find_element_by_css_selector("div[aria-label='Message Body']").send_keys("MESSAGE!")
    pyautogui.hotkey('ctrl', 'enter')
    sleep(3)

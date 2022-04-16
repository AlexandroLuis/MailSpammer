from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import pyautogui

driver = webdriver.Chrome(executable_path="C:/location/chromedriver")

Accounts = ['', '', '']
Passes = ['', '', '']
Target = 'Target to Mail Spam'
Subject = 'Subject'
Message = 'Message'

for accounts in Accounts:
    passes = Passes.pop()
    driver.get("https://stackoverflow.com/users/signup?ssrc=head&returnurl=%2Fusers%2Fstory%2Fcurrent%27")
    sleep(3)
    driver.find_element_by_xpath('//*[@id="openid-buttons"]/button[1]').click()

    driver.find_element_by_xpath('//input[@type="email"]').send_keys(accounts)
    driver.find_element_by_xpath('//*[@id="identifierNext"]').click()
    sleep(3)
    
    driver.find_element_by_xpath('//input[@type="password"]').send_keys(passes)
    pyautogui.press('enter')
    sleep(3)

    driver.get("https://mail.google.com")
    sleep(5)

    for j in range(3):
        driver.get("https://mail.google.com/mail/u/0/#inbox?compose=new")
        sleep(10)
        driver.find_element_by_class_name("vO").send_keys(Target)
        driver.find_element_by_class_name("aoT").send_keys(Subject)
        driver.find_element_by_css_selector("div[aria-label='Message Body']").send_keys(Message)
        pyautogui.hotkey('ctrl', 'enter')
        sleep(3)

#!/usr/bin/python

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
# profile path found in chrome://version/
chrome_options.add_argument("--user-data-dir=/home/bosas/.config/google-chrome/Default/Profile 1") # change to profile path
#chrome_options.add_argument('--profile-directory=Profile 1')

browser = webdriver.Chrome(executable_path="/usr/bin/chromedriver", chrome_options=chrome_options) # change the executable_path too
browser.get("https://orteil.dashnet.org/cookieclicker/")
time.sleep(3)

with open('my_cookie_id', 'r') as file:
    my_cookie_id = file.read().replace('\n', '')
    file.close()

cookie_options = browser.find_element_by_id("prefsButton")
cookie_options.click()
time.sleep(2)
cookie_import = browser.find_element_by_xpath("//div[@id='menu']/div[3]/div[3]/a[2]")
cookie_import.click()
cookie_text_id = browser.find_element_by_xpath("//div[@id='promptContent']/div[2]/textarea")
cookie_text_id.send_keys(my_cookie_id)

cookie_import_save = browser.find_element_by_xpath("//div[11]/div/div/div[3]/a")
cookie_import_save.click()

time.sleep(1)
cookie = browser.find_element_by_id("bigCookie")

sleep_time = 5
cookie_sheet = 10000
while True:
    for i in range(0, cookie_sheet):
        #time.sleep(.1)
        cookie.click()
    time.sleep(1)
    print("save {} cookies in my cookie sheet".format(cookie_sheet))
    cookie_save = browser.find_element_by_link_text("Save")
    cookie_save.click()
    time.sleep(1)
    cookie_save.click()
    export_save = browser.find_element_by_link_text("Export save")
    export_save.click()
    export_txt = browser.find_element_by_id('textareaPrompt')
    my_cookie_id = export_txt.text
    f = open("my_cookie_id", "w")
    f.write(str(my_cookie_id))
    f.close
    all_done = browser.find_element_by_id("promptOption0")
    # //*[@id="promptOption0"]
    # /html/body/div[2]/div[2]/div[11]/div/div[1]/div[3]/a
    all_done.click()
    print("data saved to file, my_cookie_id")

    time.sleep(sleep_time)

# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# import time
#
# # Replace below path with the absolute path
# # to chromedriver in your computer
# driver = webdriver.Chrome('/home/i7-workstation/Downloads/chromedriver')
#
# driver.get("https://web.whatsapp.com/")
# wait = WebDriverWait(driver, 600)
#
# # Replace 'Friend's Name' with the name of your friend
# # or the name of a group
# target = '"Vater Ruft An"'
#
# # Replace the below string with your own message
# string = "Hail me fat man!!!"
#
# x_arg = '//span[contains(@title,' + target + ')]'
# group_title = wait.until(EC.presence_of_element_located((
#     By.XPATH, x_arg)))
# group_title.click()
# inp_xpath = '//div[@class="input"][@dir="auto"][@data-tab="1"]'
# input_box = wait.until(EC.presence_of_element_located((By.XPATH, inp_xpath)))
# for i in range(100):
#     input_box.send_keys(string + Keys.ENTER)
#     time.sleep(1)
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time as t1
name=""
time=""
date = ""
f = open("Mytest.txt","r")
# def getdat(na,ti,da):
#     name = na
#     time = ti
#     date = da
x = f.read()
name,time,date = x.split(",")
# name = x[0]


def send_message():
    driver = webdriver.Chrome("/home/i7-workstation/Downloads/chromedriver")
    print("reached")
    driver.get("https://web.whatsapp.com/")
    wait = WebDriverWait(driver,600)
    message = "The appointment is booked for "
    string = message+date+" on "+time
    target =  '"ParthPatel"'
    # target = '"D.B.M.S project"'
    # target= '"'+name+'"'
    print(target)
    # target = name

    # string = "Hail me"
    x_arg = '//span[contains(@title, '+target+')]'
    target = wait.until(EC.presence_of_element_located((By.XPATH,x_arg)))
    target.click()

    input_box = driver.find_element_by_class_name('_1Plpp')
    for i in range(2):
        input_box.send_keys(string+Keys.ENTER)
        t1.sleep(1)

# send_message()
if __name__ == '__main__':
    send_message()
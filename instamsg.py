from selenium import webdriver
import string
import random
letters = string.ascii_letters

driver = webdriver.Chrome()
driver.get('https://instagram.com/direct/inbox')

# Wait until page loads
driver.implicitly_wait(20)

#Getting Credentials from user
uname = input("Enter username: ")
pword = input("Enter Password: ")


#Finding input element for username
username1 = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
username1.send_keys(uname)

#Finding input element for password
password1 = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
password1.send_keys(pword)

driver.implicitly_wait(20)

password1.submit()


driver.implicitly_wait(20)

#clicking on not now on 'save info dialogue'
btn = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button')
btn.click()

#clicking on not now for 'Turn on notifications'
ntnow = driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div[3]/button[2]')
ntnow.click()


#Getting the first user in the inbox(most recent chat)
msgbox = driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/div[1]/a/div')
msgbox.click()


driver.implicitly_wait(10)

#Message for 20 times
for i in range(100):
    msg = 'mg'

    send_message = driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')

    send_message.send_keys(msg)
    driver.implicitly_wait(10)
    send = driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button')
    send.click()
    driver.implicitly_wait(70)

driver.close()

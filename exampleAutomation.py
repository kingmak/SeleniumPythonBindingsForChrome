#an automated login for facebook
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os, time
 
usr = "fcbk email login here"
pwd = "fcbk password here"
 
driver = webdriver.Chrome(executable_path = "PATH TO CHROME DIRVER/chromedriver")
#if the chromedriver is the same directory as this script then u dont need to provide the executable_path
#like this: driver = webdriver.Chrome()

driver.get("http://www.facebook.org") #tell driver to go to fcbk
assert "Facebook" in driver.title #check if site title has string Facebook in it. you can print driver.title

elem = driver.find_element_by_id("email") #finding email box
elem.send_keys(usr) #filling in email

elem = driver.find_element_by_id("pass") #finding password box
elem.send_keys(pwd) #filling in password

elem.send_keys(Keys.RETURN) #sorta like submitting credentials

#now we should be in fcbk, the code below will attemp to write something in the status box, but it wont post it 
elem = driver.find_element_by_css_selector(".input.textInput")
elem.send_keys("This was Posted by Python :D so cool !!!")
elem = driver.find_element_by_css_selector(".selected")

#elem.click() # <-- unless that line is uncommented, the status wont be posted
time.sleep(5) # a time delay so that user has time to see what is happening to the browser
 
driver.close() #this closes the browser
raw_input('Done\n')

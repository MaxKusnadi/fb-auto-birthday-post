from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("http://facebook.com")
email = driver.find_element_by_name("email")
email.clear()
email.send_keys("max.kusnadi@gmail.com")
pwd = driver.find_element_by_name("pass")
pwd.clear()
pwd.send_keys("")
pwd.send_keys(Keys.RETURN)
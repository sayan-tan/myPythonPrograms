from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Variable Declaration
user_email = input('Enter email : ')

# Set Executable for Firefox Browser (Linux only.)
executable_path="./geckodriver"

# Opening Browser & Passing the URL to open the form.
driver = webdriver.Firefox()
driver.get("https://facebook.com")

# Checking conditions.
if user_email == "" :
    element = driver.find_element_by_id("email")
    element.send_keys()    

else :
    element = driver.find_element_by_id("email")
    element.send_keys(user_email)

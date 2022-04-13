from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

service = Service("C:\Development\chromedriver")
driver = webdriver.Chrome(service=service)

driver.get("https://github.com")
driver.maximize_window()

sign_button = driver.find_element(By.LINK_TEXT, "Sign in")
sign_button.click()

login = driver.find_element(By.ID, "login_field")
login.send_keys("my_fake_login")

password = driver.find_element(By.ID, "password")
password.send_keys("my_fake_password")
password.send_keys(Keys.ENTER)

assert "rezabekd" in driver.page_source

driver.quit()

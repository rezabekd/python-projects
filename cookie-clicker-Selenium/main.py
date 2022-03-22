from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

service = Service("C:\Development\chromedriver")
driver = webdriver.Chrome(service=service)

driver.get("http://orteil.dashnet.org/experiments/cookie/")

# cookie = driver.find_element(By.CSS_SELECTOR, "div #cookie")
cookie = driver.find_element(By.ID, "cookie")
timeout = time.time() + 15
time_end = time.time() + 600


# money_string = driver.find_element(By.ID, "money")
# current_money = int(money_string.text)
# grandma = driver.find_element(By.ID, "buyGrandma")
# grandma_string = grandma.text
# grandma_cost = int(grandma_string.split()[2])

game_going = True

while game_going:
    grandma = driver.find_element(By.ID, "buyGrandma")
    grandma_class = grandma.get_attribute("class")
    factory = driver.find_element(By.ID, "buyFactory")
    factory_class = factory.get_attribute("class")
    mine = driver.find_element(By.ID, "buyMine")
    mine_class = mine.get_attribute("class")
    shipment = driver.find_element(By.ID, "buyShipment")
    shipment_class = shipment.get_attribute("class")
    cookies = driver.find_element(By.ID, "cps")
    cps = cookies.text

    cookie.click()
    if time.time() > time_end:
        game_going = False
        print(cps)

    if time.time() > timeout:
        time.sleep(3)
        if shipment_class != "grayed":
            shipment.click()
        elif mine_class != "grayed":
            mine.click()
        elif factory_class != "grayed":
            factory.click()
        elif grandma_class != "grayed":
            grandma.click()

        time.sleep(2)

        timeout = time.time() + 15








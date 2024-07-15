from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


driver = Firefox()

try:

    driver.get("http://apps.local.edly.io/authn/login?next=%2F")


    time.sleep(5)


    search_box = driver.find_element(By.NAME, "emailOrUsername")
    
    search_box.send_keys("admin")


    search_box = driver.find_element(By.ID, "password")
    
    search_box.send_keys("12345")
    


    search_box.send_keys(Keys.RETURN)


    time.sleep(5)


    

finally:
    print(driver.title)

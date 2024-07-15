from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


driver = Firefox()

try:

    driver.get("http://apps.local.edly.io/authn/register?next=%2F")


    time.sleep(5)


    search_box = driver.find_element(By.NAME, "name")
    
    search_box.send_keys(By.NAME, "nomeerrado")



    search_box = driver.find_element(By.NAME, "email")
   
    search_box.send_keys(By.NAME, "email@errado,com")
    
  
    
    search_box = driver.find_element(By.NAME, "username")
    
    search_box.send_keys(By.NAME, "username com espaço")

    
    search_box = driver.find_element(By.ID, "password")
    
    search_box.send_keys("erro")



    search_box.send_keys(Keys.RETURN)


    time.sleep(3)

finally:
    print(driver.title)

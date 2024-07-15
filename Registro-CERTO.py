from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


driver = Firefox()

try:

    driver.get("http://apps.local.edly.io/authn/register?next=%2F")


    time.sleep(5)


    search_box = driver.find_element(By.NAME, "name")
    
    search_box.send_keys("Nome Formatado Corretamente")



    search_box = driver.find_element(By.NAME, "email")
   
    search_box.send_keys("emailcerto@gmail.com")
    
  
    
    search_box = driver.find_element(By.NAME, "username")
    
    search_box.send_keys("usernameCorreto")
    
    
    
    search_box = driver.find_element(By.ID, "password")
    
    search_box.send_keys("Projeto12345")
    


    search_box.send_keys(Keys.RETURN)


    time.sleep()


    

finally:
    print(driver.title)

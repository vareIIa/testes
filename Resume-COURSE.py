from selenium.webdriver import Firefox
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep


driver = Firefox()

# Precisa estar logado para acessar o link abaixo

try:

    driver.get("http://apps.local.edly.io/authn/login?next=%2F")


    sleep(2)


    search_box = driver.find_element(By.NAME, "emailOrUsername")
    
    search_box.send_keys("admin")


    search_box = driver.find_element(By.ID, "password")
    
    search_box.send_keys("12345")
    


    search_box.send_keys(Keys.RETURN)


    sleep(2)


    

finally:
    
    driver.get('http://apps.local.edly.io/learner-dashboard/')

    sleep(2)

    a = driver.find_element(By.CLASS_NAME, "btn.btn-primary")

    a.click()


    sleep(5)
    
    print(driver.title)
    
    driver.quit()

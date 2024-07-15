from selenium.webdriver import Firefox
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import random
import string

driver = Firefox()
caracteres_aleatorios = ''.join(random.choices(string.ascii_letters + string.digits, k=5))



try:

    driver.get("http://apps.avadev.tklocal.com.br/authn/login?next=%2F")


    sleep(5)


    search_box = driver.find_element(By.ID, "emailOrUsername")
    
    search_box.send_keys("admin")


    search_box = driver.find_element(By.ID, "password")
    
    search_box.send_keys("12345")
    


    search_box.send_keys(Keys.RETURN)


    sleep(5)


    

finally:
    
    driver.get('http://studio.avadev.tklocal.com.br/home/')

    sleep(2)

    a = driver.find_element(By.CLASS_NAME, "new-library-button")

    a.click()

    
    search_box = driver.find_element(By.CLASS_NAME, "new-library-name")
    
    search_box.send_keys(caracteres_aleatorios)
    
    search_box = driver.find_element(By.CLASS_NAME, "new-library-org")
    
    search_box.send_keys(caracteres_aleatorios)
    
    search_box = driver.find_element(By.CLASS_NAME, "new-library-number")
    
    search_box.send_keys(caracteres_aleatorios)
    
    search_box.send_keys(Keys.RETURN)


    sleep(2)

    
    print(driver.title)
    
    print(By.CLASS_NAME, "title-value")
    
    

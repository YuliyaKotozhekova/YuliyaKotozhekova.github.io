from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
driver = webdriver.Chrome()
driver.create_options()
driver.implicitly_wait(5)
driver.get("http://practice.automationtesting.in/")
driver.execute_script("window.scrollBy(0, 600);")
driver.find_element(By.CSS_SELECTOR, "[title='Selenium Ruby']").click()
driver.find_element(By.CSS_SELECTOR, "[href='#tab-reviews']").click()
driver.find_element(By.CLASS_NAME, "star-5").click()
comment = driver.find_element(By.ID, "comment")
comment.send_keys("Nice book!")
name = driver.find_element(By.ID, "author")
name.send_keys("Name")
email = driver.find_element(By.ID, "email")
email.send_keys("tututuru@mail.ru")
driver.find_element(By.ID, "submit").click()

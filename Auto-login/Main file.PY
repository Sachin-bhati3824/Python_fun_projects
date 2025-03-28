from selenium import webdriver
import os 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
def startBot(username,password,url):
    path = "C:/Users/ASUS/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe"
    service = Service(path)
    driver = webdriver.Chrome(service=service)
    driver.get(url)
    driver.find_element(By.NAME, "id/class/name of username").send_keys(username)
    driver.find_element(By.NAME,"id/class/name of password").send_keys(password)
    driver.find_element(By.CSS_SELECTOR, "id/class/name/css selector of login button").click()

username = "tomsmith"
password = "SuperSecretPassword"
url = "https://the-internet.herokuapp.com/login"

startBot(username, password, url)
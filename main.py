import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from selenium.common.exceptions import NoSuchElementException
import urllib


PATH = "C:\\Users\\mufti\\OneDrive\\Documents\\GitHub\\Reddit\\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://www.reddit.com/r/memes/")
sleep(5)

image = driver.find_element(By.CSS_SELECTOR, '[alt="Post image"]').get_attribute("src")
urllib.request.urlretrieve(image, "meme.jpg")
print("IMAGE DOWNLOADED!")
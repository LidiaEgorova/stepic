from selenium import webdriver
import time
try:
    link = "http://suninjuly.github.io/registration2.html"
    #link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--user-data-dir=chrome-data")


import os
import time
import wget



film = input()
os.system


driver = webdriver.Chrome('C:/Users/heitorzin/downloads/chromedriver_win32/chromedriver.exe', options=chrome_options)
driver.get('https://torrentool.org/')
def fechar():
    ad = WebDriverWait(driver, 4).until(EC.element_to_be_clickable((By.XPATH, "/html/body"))).click()  
    janelaoriginal = driver.current_window_handle
    driver.switch_to.window(janelaoriginal)
fechar()

find = WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='palavraPesquisa']")))

aaa = film
find.send_keys(aaa)
find.send_keys(Keys.ENTER)

pageiffm = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='capas_pequenas']/div"))).click()

html = driver.find_element_by_tag_name('html')
html.send_keys(Keys.PAGE_DOWN)
goto = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='lista_download']/a[1]"))).click()

downloadpage = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='lista_download']/a[1]"))).click()

fechar()

time.sleep(3)

driver.quit()







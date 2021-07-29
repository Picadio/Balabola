from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains
from bs4 import BeautifulSoup
from webdriver_manager.utils import ChromeType

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get('https://yandex.ru/lab/yalm')

cl = driver.find_element_by_xpath('//*[@id="app"]/div/div/button').click()

login = driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[3]/span/span[2]/textarea').send_keys("Привет как дела")

button = driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/button')
driver.execute_script("arguments[0].click();", button)


soup = BeautifulSoup(driver.page_source, 'lxml')
print(soup.div)


from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains



driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get('https://yandex.ru/lab/yalm')

cl = driver.find_element_by_xpath('//*[@id="app"]/div/div/button').click()

login = driver.find_element_by_xpath("//*[@id="app"]/div/div[2]/div[3]/span/span[2]/textarea").send_keys("Hello")

button = driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/button')
button.click()

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from read import tobuy
import time

SECOND_PASS = '111222'


def buy(driver: webdriver.Chrome(), item: str, amount: int) -> None:
    driver.find_element(By.CSS_SELECTOR, 'input#txtItemName').send_keys(item)
    driver.find_element(By.CSS_SELECTOR, 'button.button--deal-submit').click()
    time.sleep(0.5)
    driver.find_element(By.CSS_SELECTOR, 'button.button--deal-buy').click()
    time.sleep(0.8)
    quantity = driver.find_element(By.CSS_SELECTOR, 'input.quantity')
    # quantity.send_keys(Keys.RIGHT)
    # quantity.send_keys(Keys.DELETE)
    # quantity.send_keys(amount)
    up = driver.find_element(By.CSS_SELECTOR, 'button.button--up')
    for _ in range(amount - 1):
        up.click()
    driver.execute_script('arguments[0].click()', driver.find_element(By.XPATH, '//*[@id="agreed"]'))
    driver.find_element(By.CSS_SELECTOR, 'button.lui-modal__buy').click()
    time.sleep(0.8)
    buttons = driver.find_elements(By.CSS_SELECTOR, 'button.button--password-num')
    for i in SECOND_PASS:
        for button in buttons:
            if button.text == i:
                button.click()
                break
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, 'button.button--password-confirm').click()
    time.sleep(0.8)
    driver.find_element(By.CSS_SELECTOR, 'button.lui-modal__confirm').click()
    driver.find_element(By.CSS_SELECTOR, 'button.button--itemdic-delete').click()


otp = int(input("OTP 입력: "))
options = webdriver.ChromeOptions()
# options.add_argument("headless")
driver = webdriver.Chrome(service=Service('./chromedriver.exe'), options=options)
driver.get('https://lostark.game.onstove.com/Market')
time.sleep(0.8)
ID = driver.find_element(By.CSS_SELECTOR, 'input#id')
PASS = driver.find_element(By.CSS_SELECTOR, 'input#password')
time.sleep(0.3)
driver.maximize_window()
ID.send_keys('whgnlwjd1@naver.com')
PASS.send_keys('Whgnlwjd1!')
PASS.send_keys(Keys.ENTER)
time.sleep(0.8)
driver.find_element(By.CSS_SELECTOR, 'input#otpCode').send_keys(otp)
driver.find_element(By.CSS_SELECTOR, 'input#otpCode').send_keys(Keys.ENTER)
time.sleep(0.8)
for i in tobuy:
    buy(driver, i[0], int(i[1]))
time.sleep(5)

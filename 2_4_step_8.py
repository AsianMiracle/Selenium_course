from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))



with webdriver.Chrome() as browser:

    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    waited = WebDriverWait(browser, 12).until(
            EC.text_to_be_present_in_element ((By.ID, "price"), '$100')
        )
    browser.find_element_by_xpath("//button[@id='book']").click()

    x_var = browser.find_element_by_xpath("//span[@id='input_value']").text
    browser.find_element_by_xpath("//input[@id='answer']").send_keys(calc(x_var))
    browser.find_element_by_xpath("//button[@id='solve']").click()

    answer = browser.switch_to.alert.text.split(': ')[-1]
    print(answer)

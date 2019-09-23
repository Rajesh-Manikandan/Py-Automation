from selenium import webdriver
import time

from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(
    executable_path="C:/Users/Rajesh/Downloads/chromedriver_win32/chromedriver.exe")

try:
    driver.get("http://google.com")

    assert "Google" in driver.title

    search_inp = driver.find_element_by_name("q")
    search_inp.clear()
    search_inp.send_keys("Realme 5 Pro")
    search_inp.send_keys(Keys.RETURN)

    assert "realme*" in driver.title

    time.sleep(3)

finally:
    driver.quit()

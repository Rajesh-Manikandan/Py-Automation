import xlrd
import os
import time
from selenium import webdriver


# Initiate webdriver
driver = webdriver.Chrome(
    executable_path="C:/Users/Rajesh/Downloads/chromedriver_win32/chromedriver.exe")

try:
    # Open RPA Challenge Site
    driver.get("http://RPACHallenge.com",)
    assert "Rpa Challenge" in driver.title

    startBtn = driver.find_elements_by_tag_name('button')[0]

    file = "Selenium/challenge.xlsx"

    wb = xlrd.open_workbook(os.path.abspath(file))
    sh1 = wb.sheet_by_index(0)

    startBtn.click()
    print(sh1.nrows)
    for row_num in range(1, sh1.nrows):
        # Find Elements
        FirstName = driver.find_element_by_xpath(
            "//*[contains(text(), 'First Name')]/following-sibling::input")
        LastName = driver.find_element_by_xpath(
            "//*[contains(text(), 'Last Name')]/following-sibling::input")
        RoleInCompany = driver.find_element_by_xpath(
            "//*[contains(text(), 'Role in Company')]/following-sibling::input")
        Address = driver.find_element_by_xpath(
            "//*[contains(text(), 'Address')]/following-sibling::input")
        CompanyName = driver.find_element_by_xpath(
            "//*[contains(text(), 'Company Name')]/following-sibling::input")
        PhoneNumber = driver.find_element_by_xpath(
            "//*[contains(text(), 'Phone Number')]/following-sibling::input")
        Email = driver.find_element_by_xpath(
            "//*[contains(text(), 'Email')]/following-sibling::input")
        submitBtn = driver.find_element_by_xpath("//input[@type='submit']")
        for col_num in range(sh1.ncols):
            value = sh1.cell_value(row_num, col_num)
            if col_num == 0:
                FirstName.send_keys(value)
            elif col_num == 1:
                LastName.send_keys(value)
            elif col_num == 2:
                CompanyName.send_keys(value)
            elif col_num == 3:
                RoleInCompany.send_keys(value)
            elif col_num == 4:
                Address.send_keys(value)
            elif col_num == 5:
                Email.send_keys(value)
            else:
                PhoneNumber.send_keys(str(value))
        print(row_num)
        submitBtn.click()

finally:
    time.sleep(10)
    driver.quit()

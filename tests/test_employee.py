import time

from selenium.webdriver.common.by import By

from tests.test_inheritence import WebdriverWrapper


class TestAddEmployee(WebdriverWrapper):
    def test_add_valid_employee(self):
        print("Add Employee Details")
        self.driver.find_element(By.NAME, "username").send_keys("admin")
        self.driver.find_element(By.NAME, "password").send_keys("admin123")
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
        self.driver.find_element(By.XPATH, "//span[text()='PIM']").click()
        self.driver.find_element(By.LINK_TEXT, "Add Employee").click()
        time.sleep(5)
        self.driver.find_element(By.NAME, "firstName").send_keys("John")

        self.driver.find_element(By.NAME, "middleName").send_keys("k")

        self.driver.find_element(By.NAME, "lastName").send_keys("Sagar")
        time.sleep(10)
        ele = "//label[text()='Employee Id']/following::input[@class='oxd-input oxd-input--active']"
        self.driver.execute_script("argument[0].value=988", ele)
        # action = WebDriver.
        # self.driver.find_element(By.XPATH, "//label[text()='Employee Id']/following::input[@class='oxd-input oxd-input--active']").clear()
        # self.driver.find_element(By.XPATH,
        #                          "//label[text()='Employee Id']/following::input[@class='oxd-input oxd-input--active']").send_keys("987")
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Save']").click()
        time.sleep(30)



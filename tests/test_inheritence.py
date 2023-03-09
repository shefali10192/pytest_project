import time

import pytest
from assertpy import assert_that
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from utilities import datasource

#
class WebdriverWrapper:
    # def __init__(self):
    #     print("helo")

    @pytest.fixture(scope="function", autouse=True)
    def setup(self):

        #serv_driver = Service(executable_path='C:\\Users\\112552\\Downloads\\chromedriver_win32\\chromedriver.exe')
        self.driver = webdriver.Chrome()
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        yield
        self.driver.quit()

    def test_login_placeholder(self):
        actual_u_placeholder = self.driver.find_element(By.NAME, 'username').get_attribute("placeholder")
        actual_p_placeholder = self.driver.find_element(By.NAME, 'password').get_attribute("placeholder")
        assert_that("Username").is_equal_to(actual_u_placeholder)
        assert_that("Password").is_equal_to(actual_p_placeholder)


class TestLoginUI(WebdriverWrapper):

        @pytest.mark.parametrize("username, password, expected_error", datasource.test_invalid_data )
        def test_invalid_login(self, username, password, expected_error):
            self.driver.find_element(By.NAME, "username").send_keys(username)
            self.driver.find_element(By.NAME, "password").send_keys(password)
            self.driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
            actual_error = self.driver.find_element(By.XPATH, "//p[text()='Invalid credentials']").text
            # print(actual_error)
            time.sleep(10)
            assert_that(expected_error).is_equal_to(actual_error)
        @pytest.mark.smoke
        def test_valid_login(self):
            self.driver.find_element(By.NAME, "username").send_keys("Admin")
            self.driver.find_element(By.NAME, "password").send_keys("admin123")
            self.driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
            if len(self.driver.find_elements(By.XPATH, "//h6[text()='Dashboard']")) > 0:
                print("Valid Login")


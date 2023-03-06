import time

import pytest
from assertpy import assert_that
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

#
class WebdriverWrapper:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self):

        serv_driver = Service(executable_path='C:\\Users\\112552\\Downloads\\chromedriver_win32\\chromedriver.exe')
        self.driver = webdriver.Chrome(service=serv_driver)
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        yield
        self.driver.quit()


class TestLoginUI(WebdriverWrapper):

        def test_valid_login(self):
        # self.driver.get("https://opensource-demo.orangehrmlive.com/")
        # time.sleep(30)
            self.driver.find_element(By.NAME,"username").send_keys("admin")
            self.driver.find_element(By.NAME, "password").send_keys("admin123")
            self.driver.find_element(By.XPATH,"//button[normalize-space()='Login']").click()
            checked = self.driver.find_element(By.XPATH, "//h6[normalize-space()='Dashboard']").text
            assert_that("Dashboard").is_equal_to(checked)




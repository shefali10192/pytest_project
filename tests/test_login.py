import time

import pytest
from assertpy import assert_that
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


class TestLoginUI:
    @pytest.fixture(scope="function")
    def setup(self):
        print("hi")
        serv_driver = Service(executable_path='C:\\Users\\112552\\Downloads\\chromedriver_win32\\chromedriver.exe')
        self.driver = webdriver.Chrome(service = serv_driver)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        yield
        self.driver.quit()
    def test_title(self, setup):
        print("Shefali")
        self.driver.get("https://www.google.com/")
        actual_title = self.driver.title
        print(actual_title)
        # assert 'Goo' in actual_title
        # assert actual_title == "Google"
        assert_that("Google").is_equal_to(actual_title)

    def test_header(self, setup):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        text = self.driver.find_element(By.XPATH, "//h5[text()='Login']").text
        assert_that("Login").is_equal_to(text)


    def test_demo(self, setup):
        print("Test Demo: without launch the Browser")
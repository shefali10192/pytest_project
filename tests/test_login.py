import time

import pytest
from assertpy import assert_that
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

#
class TestLogin:
    @pytest.fixture(scope="class", autouse=True)
    def class_scope(self):
        print("Class triggered")
        yield
        print("Class End")

    def test_valid_login1(self):
        print("Valid Login")
    def test_invalid_login1(self):
        print("Invalid Login")


class TestLoginUI:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self):

        serv_driver = Service(executable_path='C:\\Users\\112552\\Downloads\\chromedriver_win32\\chromedriver.exe')
        self.driver = webdriver.Chrome(service=serv_driver)
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        yield
        self.driver.quit()


    def test_title(self):
        print("Shefali")
        self.driver.get("https://www.google.com/")
        actual_title = self.driver.title
        print(actual_title)
        # assert 'Goo' in actual_title
        # assert actual_title == "Google"
        assert_that("Google").is_equal_to(actual_title)

    def test_header(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        text = self.driver.find_element(By.XPATH, "//h5[text()='Login']").text
        assert_that("Login").is_equal_to(text)


    def test_demo(self):
        print("Test Demo: without launch")

    def test_valid_login(self):
        # self.driver.get("https://opensource-demo.orangehrmlive.com/")
        # time.sleep(30)
        self.driver.find_element(By.NAME,"username").send_keys("admin")
        self.driver.find_element(By.NAME, "password").send_keys("admin123")
        self.driver.find_element(By.XPATH,"//button[normalize-space()='Login']").click()
        checked = self.driver.find_element(By.XPATH, "//h6[normalize-space()='Dashboard']").text
        assert_that("Dashboard").is_equal_to(checked)




from assertpy import assert_that
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


class TestLoginUI:
    def test_title(self):
        serv_driver = Service(executable_path='C:\\Users\\112552\\Downloads\\chromedriver_win32\\chromedriver.exe')
        driver = webdriver.Chrome(service = serv_driver)
        driver.maximize_window()
        driver.get("https://www.google.com/")
        actual_title = driver.title
        print(actual_title)
        # assert 'Goo' in actual_title
        # assert actual_title == "Google"
        assert_that("Google").is_equal_to(actual_title)

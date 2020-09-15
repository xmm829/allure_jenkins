import allure
from selenium import webdriver
import time


class Test_001:
    def setup_class(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://www.baidu.com")

    def teardown_class(self):
        time.sleep(2)
        self.driver.quit()

    @allure.step("第二步")
    def abc(self):
        print("123")

    @allure.step("第一步")
    def test_01(self):
        self.abc()
        allure.attach(self.driver.get_screenshot_as_png(), "截图", allure.attachment_type.PNG)
        print("\n test_001")

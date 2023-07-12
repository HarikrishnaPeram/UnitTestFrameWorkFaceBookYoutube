from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import unittest
class SignupTest (unittest.TestCase):

    @classmethod
    def setup(cls):
        cls.driver = webdriver.Chrome(executable_path="C:/Users/selenium/work space/chromedriver.exe")
        cls.driver.get("https://www.facebook.com/signup")
        cls.driver.implicitly_wait(5)
        cls.driver.maximize_window()
    def test_signup_Valid(self):
        #self.signup=SignupTest.SP()
        self.driver.find_element(By.XPATH, "//input[@name='firstname']").send_keys("Hari")
        self.driver.find_element(By.XPATH, "//input[@name='lastname']").send_keys("Krishna")
        self.driver.find_element(By.XPATH, "//input[@name='reg_email__']").send_keys(9876543210)
        self.driver.find_element(By.CSS_SELECTOR, "#password_step_input").send_keys("Harikrishna141")
        Daydropdown = Select(self.driver.find_element(By.CSS_SELECTOR, "#day"))
        Daydropdown.select_by_index(1)
        Monthdropdown = Select(self.driver.find_element(By.CSS_SELECTOR, "#month"))
        Monthdropdown.select_by_index(1)
        Yeardropdown = Select(self.driver.find_element(By.CSS_SELECTOR, "#year"))
        Yeardropdown.select_by_index(10)
        self.driver.find_element(By.XPATH, "//input[@value='2']").click()
        self.driver.find_element(By.NAME, "websubmit").click()

    @classmethod
    def teardownclass(cls):
        cls.driver.close()
        print("Test Executed")
if __name__=='__main__':
    if __name__ == '__main__':
        unittest.main

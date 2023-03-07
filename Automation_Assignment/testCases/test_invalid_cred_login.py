import os
import time
from selenium.common import TimeoutException
from pageObjects.LoginInvalidCredential import LoginInvalidCredPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import SingletonLogger


class Test_Invalid_Cred_Login:
    baseUrl = ReadConfig().getApplicationUrl()
    username = ReadConfig().getUserName()
    password = ReadConfig().getPassword()
    invalid_username = ReadConfig.getInvalidUsername()
    logger = SingletonLogger()

    def test_invalid_cred_login(self, setup):
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()
        self.logger.log_info('Logging in with invalid credentials on Saucelabs')
        ic = LoginInvalidCredPage(self.driver)
        ic.setInvalidUserName(self.invalid_username)
        ic.setInvalidPassword(self.password)
        ic.clickSubmit()
        try:
            err_msg = ic.getErrorMessage()
            assert err_msg.is_displayed()
            self.logger.log_info("Logging with invalid credentials successful")
            screenshot_path = os.path.abspath(os.path.join(os.getcwd(), "..", "Screenshots", "loginpage.png"))
            self.driver.save_screenshot(screenshot_path)
        except TimeoutException:
            self.logger.log_info("Logging with valid credentials successful")
            screenshot_path = os.path.abspath(os.path.join(os.getcwd(), "..", "Screenshots", "homepage.png"))
            self.driver.save_screenshot(screenshot_path)
            self.logger.log_error("Logging with invalid credentials failed")
        finally:
            time.sleep(3)


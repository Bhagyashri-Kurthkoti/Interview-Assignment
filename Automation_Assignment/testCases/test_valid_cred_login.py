import os
import time
from selenium.webdriver.common.by import By
from pageObjects.LoginSignUp import SignUpPage
from utilities import random_user_credentials
from utilities.readProperties import ReadConfig
from utilities.customLogger import SingletonLogger


class Test_Valid_Cred_Login:
    baseUrl = ReadConfig().getApplicationUrl()
    username = ReadConfig().getUserName()
    password = ReadConfig().getPassword()
    invalid_username = ReadConfig.getInvalidUsername()
    email = random_user_credentials.generate_random_email()
    first_name = random_user_credentials.generate_random_first_name()
    last_name = random_user_credentials.generate_random_last_name()
    random_password = random_user_credentials.generate_random_password()
    postal_code = random_user_credentials.generate_random_pincode()
    signup_options_locator = (By.CSS_SELECTOR, ".signup-option")
    google_signup_locator = (By.CSS_SELECTOR, ".google")
    github_signup_locator = (By.CSS_SELECTOR, ".github")
    email_signup_locator = (By.CSS_SELECTOR, ".email")
    name_field_locator = (By.NAME, "name")
    logger = SingletonLogger()

    def test_login(self, setup):
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.baseUrl)
        self.logger.log_info('Logging in with valid credentials on Saucelabs')
        sp = SignUpPage(self.driver)
        sp.setUserName(self.username)
        sp.setPassword(self.password)
        sp.clickSubmit()
        self.products_title = sp.verifyPageTitle()
        if self.driver.title == self.products_title:
            self.logger.log_info("Logged in successfully")
            assert "Successfully logged in"
        else:
            screenshot_path = os.path.abspath(os.path.join(os.getcwd(), "..", "Screenshots", "login_page.png"))
            self.driver.save_screenshot(screenshot_path)
            self.logger.log_error('An error occurred,please try with valid credentials')
        time.sleep(3)



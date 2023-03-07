import os
import time
from pageObjects.LoginSignUp import SignUpPage
from utilities import random_user_credentials
from utilities.readProperties import ReadConfig
from utilities.customLogger import SingletonLogger


class Test_Signup:
    baseUrl = ReadConfig().getApplicationUrl()
    username = ReadConfig().getUserName()
    password = ReadConfig().getPassword()
    invalid_username = ReadConfig.getInvalidUsername()
    email = random_user_credentials.generate_random_email()
    first_name = random_user_credentials.generate_random_first_name()
    last_name = random_user_credentials.generate_random_last_name()
    random_password = random_user_credentials.generate_random_password()
    postal_code = random_user_credentials.generate_random_pincode()
    logger = SingletonLogger()

    def test_select_signup_option(self, setup):
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.baseUrl)
        self.logger.log_info('Signing up on Saucelabs')
        sp = SignUpPage(self.driver)
        sp.setUserName(self.username)
        sp.setPassword(self.password)
        sp.clickSubmit()
        time.sleep(3)
        sp.clickMenu()
        sp.clickAbout()
        sp.clickTryItForFree()
        self.logger.log_info('Selecting a random signup option')
        option = sp.chooseRandomSignUpOption()
        if option[0] == 'Sign up with Google':
            self.logger.log_info(f"option selected is {option}")
            self.sign_up_with_google(setup)
        elif option[0] == 'Sign up with GitHub':
            self.logger.log_info(f"option selected is {option}")
            self.sign_up_with_github(setup)
        else:
            self.logger.log_info(f"option selected is {option}")
            self.sign_up_with_email(setup)

    def sign_up_with_google(self, setup):
        self.driver = setup
        sp = SignUpPage(self.driver)
        self.driver.implicitly_wait(10)
        sp.clickSignUpWithGoogle()
        try:
            sp.setSignUpEmail()
            sp.clickNext()
            time.sleep(3)
            sp.setGmailSignUpPassword()
            sp.clickLogin()
        except:
            screenshot_path = os.path.abspath(
                os.path.join(os.getcwd(), "..", "Screenshots", "Sign_up_error_Google.png"))
            self.driver.save_screenshot(screenshot_path)
            self.logger.log_error("Invalid credentials , please try with valid credentials")
        time.sleep(3)
        self.signup_page_title = sp.verifySignUpPageTitle() + " | Sauce Labs"
        if self.driver.title == self.signup_page_title:
            assert "Sign up successful"
            self.logger.log_info("Sign Up with Google successful")
        else:
            self.logger.log_error("Sign up with Google unsuccessful")
            assert "Sign up unsuccessful"

    def sign_up_with_github(self, setup):
        self.driver = setup
        sp = SignUpPage(self.driver)
        self.driver.implicitly_wait(10)
        sp.clickSignUpWithGithub()
        try:
            sp.setGithubSignUpEmail()
            time.sleep(3)
            sp.setGithubSignUpPassword()
            sp.clickGithubSubmit()
            authorize_button = sp.clickAuthorize()
            if authorize_button is None:
                print("Account Authorized")
            else:
                authorize_button.click()
                print("Account Authorization must be done")
        except:
            screenshot_path = os.path.abspath(
                os.path.join(os.getcwd(), "..", "Screenshots", "Sign_up_error_Github.png"))
            self.driver.save_screenshot(screenshot_path)
            self.logger.log_error("Invalid credentials , please try with valid credentials")
        time.sleep(3)
        self.signup_page_title = sp.verifySignUpPageTitle() + " | Sauce Labs"
        if self.driver.title == self.signup_page_title:
            assert "Sign up successful"
            self.logger.log_info("Sign Up with Github successful")
        else:
            self.logger.log_error("Sign up with Github unsuccessful")
            assert "Sign up unsuccessful"

    def sign_up_with_email(self, setup):
        self.driver = setup
        sp = SignUpPage(self.driver)
        self.driver.implicitly_wait(10)
        sp.clickSignUpWithEmail()
        sp.setEmail(self.email)
        sp.setSignUpUserName(self.first_name)
        sp.setSignUpPassword(self.random_password)
        sp.clickSubscription()
        sp.clickSignUp()
        time.sleep(3)
        try:
            self.signup_page_title = sp.verifySignUpPageTitle() + " | Sauce Labs"
        except:
            screenshot_path = os.path.abspath(os.path.join(os.getcwd(), "..", "Screenshots", "Sign_up_error_email.png"))
            self.driver.save_screenshot(screenshot_path)
            self.logger.log_error("Invalid credentials , please try with valid credentials")
        if self.driver.title == self.signup_page_title:
            assert "Sign up successful"
            self.logger.log_info("Sign Up with email successful")
        else:
            self.logger.log_error("Sign up with email unsuccessful")
            assert "Sign up unsuccessful"

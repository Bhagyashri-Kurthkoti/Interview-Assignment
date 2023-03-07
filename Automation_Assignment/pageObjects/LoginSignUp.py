import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from utilities.readProperties import ReadConfig


class SignUpPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.textbox_login_username_id = (By.ID, "user-name")
        self.textbox_login_password_id = (By.ID, "password")
        self.button_submit_id = (By.ID, "login-button")
        self.link_menu_id = (By.ID, "react-burger-menu-btn")
        self.link_about_xpath = (By.XPATH, "//a[@id='about_sidebar_link']")
        self.link_sign_in_text = (By.LINK_TEXT, "Sign in")
        self.frame_cookies_class = (By.CLASS_NAME, "drift-frame-controller")
        self.button_accept_all_cookies_id = (By.ID, "onetrust-accept-btn-handler")
        self.link_tryitforfree_linktext = (By.LINK_TEXT, "Try it free")
        self.linktext_Signupwithemail_text = (By.LINK_TEXT, "Sign up with email")
        self.textbox_email_id = (By.ID, "email")
        self.textbox_signup_username_id = (By.ID, "username")
        self.textbox_signup_password_id = (By.ID, "password")
        self.checkbox_subscription_id = (By.ID, "subscription")
        self.button_signup_xpath = (By.XPATH, "//button[@type='submit']")
        self.link_signup_page_title_xpath = (By.XPATH,
                                             "//span[@class='text-medium-emphasis font-semibold text-high-emphasis "
                                             "Typography__body-large__a8hFM font-sans']")
        self.link_signup_with_google_xpath = (By.XPATH, "//a[@title='Authenticate with Google']")
        self.textbox_sign_up_email_id_xpath = (By.XPATH, "//input[@id='identifierId']")
        self.button_next_id = (By.ID, "identifierNext")
        self.textbox_sign_up_password_css_selector = (By.CSS_SELECTOR, "input[type=password]")
        self.button_login_id = (By.ID, "passwordNext")
        self.link_signup_with_github_xpath = (By.XPATH, "//a[@title='Authenticate with Github']")
        self.textbox_git_email_id_id = (By.ID, "login_field")
        self.textbox_git_password_id = (By.ID, "password")
        self.button_sign_in_css_selector = (By.CSS_SELECTOR, "input[type=submit]")
        self.button_authorize_xpath = (By.XPATH, "//button[@id='js-oauth-authorize-btn']")
        self.button_locator_xpath = (By.XPATH,
                                     "//ul[@class='SignupOptions_list-inline___VEyt']/li/a[contains(.,'Sign up "
                                     "with')]")
        self.valid_email_id = ReadConfig.setValid_Email()
        self.valid_email_password = ReadConfig.setValid_Email_Password()
        self.invalid_email = ReadConfig.setInvalid_Email()
        self.valid_git_password = ReadConfig.setValid_Git_Password()
        self.invalid_git_password = ReadConfig.setInvalid_Git_Password()

    def setUserName(self, username):
        self.wait.until(EC.presence_of_element_located(self.textbox_login_username_id)).send_keys(username)

    def setPassword(self, password):
        self.wait.until(EC.presence_of_element_located(self.textbox_login_password_id)).send_keys(password)

    def clickSubmit(self):
        self.wait.until(EC.element_to_be_clickable(self.button_submit_id)).click()

    def verifyPageTitle(self):
        return self.driver.title

    def clickMenu(self):
        self.wait.until(EC.element_to_be_clickable(self.link_menu_id)).click()

    def clickAbout(self):
        self.wait.until(EC.element_to_be_clickable(self.link_about_xpath)).click()

    def clickSignIn(self):
        self.wait.until(EC.element_to_be_clickable(self.link_sign_in_text)).click()

    def clickAcceptAllCookies(self):
        self.wait.until(EC.element_to_be_clickable(self.button_accept_all_cookies_id)).click()

    def clickTryItForFree(self):
        self.wait.until(EC.presence_of_element_located(self.link_tryitforfree_linktext)).click()

    def clickSignUpWithEmail(self):
        self.wait.until(EC.element_to_be_clickable(self.linktext_Signupwithemail_text)).click()

    def setEmail(self, email):
        self.wait.until(EC.presence_of_element_located(self.textbox_email_id)).send_keys(email)

    def setSignUpUserName(self, new_username):
        self.wait.until(EC.presence_of_element_located(self.textbox_signup_username_id)).send_keys(new_username)

    def setSignUpPassword(self, new_password):
        self.wait.until(EC.presence_of_element_located(self.textbox_signup_password_id)).send_keys(new_password)

    def clickSubscription(self):
        self.wait.until(EC.element_to_be_clickable(self.checkbox_subscription_id)).click()

    def clickSignUp(self):
        self.wait.until(EC.element_to_be_clickable(self.button_signup_xpath)).click()

    def verifySignUpPageTitle(self):
        return self.wait.until(EC.visibility_of_element_located(self.link_signup_page_title_xpath)).text

    def clickSignUpWithGoogle(self):
        return self.wait.until(EC.element_to_be_clickable(self.link_signup_with_google_xpath)).click()

    def setSignUpEmail(self):
        return self.wait.until(EC.presence_of_element_located(self.textbox_sign_up_email_id_xpath)).send_keys(
            self.valid_email_id)

    def clickNext(self):
        return self.wait.until(EC.element_to_be_clickable(self.button_next_id)).click()

    def setGmailSignUpPassword(self):
        return self.wait.until(EC.presence_of_element_located(self.textbox_sign_up_password_css_selector)).send_keys(
            self.valid_email_password)

    def clickLogin(self):
        return self.wait.until(EC.element_to_be_clickable(self.button_login_id)).click()

    def clickSignUpWithGithub(self):
        return self.wait.until(EC.element_to_be_clickable(self.link_signup_with_github_xpath)).click()

    def setGithubSignUpEmail(self):
        return self.wait.until(EC.presence_of_element_located(self.textbox_git_email_id_id)).send_keys(
            self.valid_email_id)

    def setGithubSignUpPassword(self):
        self.user_git_password= self.wait.until(EC.presence_of_element_located(self.textbox_git_password_id))
        self.user_git_password.send_keys(self.valid_git_password)
        self.user_entered_password=self.user_git_password.get_attribute("value")
        if self.user_entered_password == self.valid_git_password:
            return self.user_git_password
        else:
            raise ValueError("Invalid password")

    def clickGithubSubmit(self):
        return self.wait.until(EC.element_to_be_clickable(self.button_sign_in_css_selector)).click()

    def clickAuthorize(self):
        try:
            return self.wait.until(EC.element_to_be_clickable(self.button_authorize_xpath))
        except:
            return None

    def chooseRandomSignUpOption(self):
        self.driver.implicitly_wait(10)
        options = self.wait.until(EC.presence_of_all_elements_located(self.button_locator_xpath))
        signup_options = [option.text for option in options]
        random_option = random.choices(signup_options)
        return random_option

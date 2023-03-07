from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class LoginInvalidCredPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.textbox_login_username_id = (By.ID, "user-name")
        self.textbox_login_password_id = (By.ID, "password")
        self.button_submit_id = (By.ID, "login-button")
        self.textbox_error_message_xpath = (By.XPATH, "//div[@class='error-message-container error']")

    def setInvalidUserName(self, username):
        self.wait.until(EC.presence_of_element_located(self.textbox_login_username_id)).send_keys(username)

    def setInvalidPassword(self, password):
        self.wait.until(EC.presence_of_element_located(self.textbox_login_password_id)).send_keys(password)

    def clickSubmit(self):
        self.wait.until(EC.element_to_be_clickable(self.button_submit_id)).click()

    def getErrorMessage(self):
        return self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='error']")))



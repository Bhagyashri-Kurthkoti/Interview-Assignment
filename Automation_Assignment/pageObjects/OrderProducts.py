from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class OrderProductsPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.textbox_login_username_id = (By.ID, "user-name")
        self.textbox_login_password_id = (By.ID, "password")
        self.button_submit_id = (By.ID, "login-button")
        self.button_add_Tshirt_to_cart_xpath = (By.XPATH, "//button[@id='add-to-cart-sauce-labs-bolt-t-shirt']")
        self.label_price_xpath = (By.XPATH, "(//div[@class='inventory_item_price'])[3]")
        self.button_add_backpack_to_cart_xpath = (By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']")
        self.link_shopping_cart_xpath = (By.XPATH, "//a[@class='shopping_cart_link']")
        self.button_checkout_id = (By.ID, "checkout")
        self.textbox_first_name_id = (By.ID, "first-name")
        self.textbox_last_name_id = (By.ID, "last-name")
        self.textbox_postal_code_id = (By.ID, "postal-code")
        self.textbox_continue_id = (By.ID, "continue")
        self.label_total_price_xpath = (By.XPATH, "//div[@class='summary_info_label summary_total_label']")
        self.button_finish_order_id = (By.ID, "finish")
        self.text_verify_order_successful_class = (By.CLASS_NAME, "complete-header")

    def setUserName(self, username):
        self.wait.until(EC.presence_of_element_located(self.textbox_login_username_id)).send_keys(username)

    def setPassword(self, password):
        self.wait.until(EC.presence_of_element_located(self.textbox_login_password_id)).send_keys(password)

    def clickSubmit(self):
        self.wait.until(EC.element_to_be_clickable(self.button_submit_id)).click()

    def addTshirtToCart(self):
        self.wait.until(EC.element_to_be_clickable(self.button_add_Tshirt_to_cart_xpath)).click()

    def assertPrice(self):
        return self.wait.until(EC.visibility_of_element_located(self.label_price_xpath)).text

    def addBackPackToCart(self):
        self.wait.until(EC.element_to_be_clickable(self.button_add_backpack_to_cart_xpath)).click()

    def clickOnCart(self):
        self.wait.until(EC.element_to_be_clickable(self.link_shopping_cart_xpath)).click()

    def checkOut(self):
        self.wait.until(EC.element_to_be_clickable(self.button_checkout_id)).click()

    def setFirstname(self, first_name):
        self.wait.until(EC.element_to_be_clickable(self.textbox_first_name_id)).send_keys(first_name)

    def setLastName(self, last_name):
        self.wait.until(EC.element_to_be_clickable(self.textbox_last_name_id)).send_keys(last_name)

    def setPostalCode(self, postal_code):
        self.wait.until(EC.element_to_be_clickable(self.textbox_postal_code_id)).send_keys(postal_code)

    def clickContinue(self):
        self.wait.until(EC.element_to_be_clickable(self.textbox_continue_id)).click()

    def assertTotalPrice(self):
        return self.wait.until(EC.visibility_of_element_located(self.label_total_price_xpath)).text

    def finishOrder(self):
        self.wait.until(EC.element_to_be_clickable(self.button_finish_order_id)).click()

    def orderStatus(self):
        return self.wait.until(EC.visibility_of_element_located(self.text_verify_order_successful_class))

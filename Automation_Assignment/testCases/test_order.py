import os
import time
from pageObjects.OrderProducts import OrderProductsPage
from utilities import random_user_credentials
from utilities.readProperties import ReadConfig
from utilities.customLogger import SingletonLogger


class Test_Order:
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

    def test_order(self, setup):
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.baseUrl)
        self.logger.log_info('Ordering products')
        pp = OrderProductsPage(self.driver)
        pp.setUserName(self.username)
        pp.setPassword(self.password)
        pp.clickSubmit()
        time.sleep(3)
        pp.addTshirtToCart()
        self.price = pp.assertPrice()
        self.exp_price = ReadConfig.getExp_Price()
        self.logger.log_info('Validating product value')
        if self.exp_price == self.price:
            assert True, f"The price displayed {self.price} is equal to expected price {self.exp_price}"
            self.logger.log_info(f"The price displayed {self.price} is equal to expected price {self.exp_price}")
        else:
            screenshot_path = os.path.abspath(os.path.join(os.getcwd(), "..", "Screenshots", "item_price.png"))
            self.driver.save_screenshot(screenshot_path)
            self.logger.log_error(
                f"The price displayed ({self.price}) is not equal to expected price ({self.exp_price})")
            assert False, f"The price displayed ({self.price}) is not equal to expected price ({self.exp_price})"
        pp.addBackPackToCart()
        pp.clickOnCart()
        pp.checkOut()
        pp.setFirstname(self.first_name)
        pp.setLastName(self.last_name)
        pp.setPostalCode(self.postal_code)
        pp.clickContinue()
        self.total_price = pp.assertTotalPrice()
        self.exp_total_price = "Total: " + ReadConfig.getTotal_Exp_Price()
        self.logger.log_info('Validating cart value')
        if self.total_price == self.exp_total_price:
            assert True, f"The total price of the order ({self.total_price}) is equal to expected price ({self.exp_total_price})"
            self.logger.log_info(
                f"The total price of the order ({self.total_price}) is equal to expected price ({self.exp_total_price})")
        else:
            self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
            screenshot_path = os.path.abspath(os.path.join(os.getcwd(), "..", "Screenshots", "exp_total_price.png"))
            self.driver.save_screenshot(screenshot_path)
            self.logger.log_error(
                f"The total price of the order ({self.total_price}) is not equal to expected price ({self.exp_total_price})")
            assert False, f"The total price of the order ({self.total_price}) is not equal to expected price ({self.exp_total_price})"
        pp.finishOrder()
        msg = pp.orderStatus()
        try:
            assert msg.is_displayed(), "Order successful"
            self.logger.log_info("Order Successful")
        except AssertionError:
            screenshot_path = os.path.abspath(os.path.join(os.getcwd(), "..", "Screenshots", "order_error.png"))
            self.driver.save_screenshot(screenshot_path)
            self.logger.log_error("Order unsuccessful")
        finally:
            time.sleep(3)

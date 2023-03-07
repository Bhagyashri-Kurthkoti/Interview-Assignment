import configparser
from configparser import ConfigParser
import os
import Configurtions

config = configparser.RawConfigParser()
config_path = os.path.abspath(os.path.join(os.getcwd(), "..", "Configurtions", "config.ini"))
config.read(config_path)


class ReadConfig:
    @staticmethod
    def getApplicationUrl():
        url = config.get('Info', 'baseUrl')
        return url

    @staticmethod
    def getUserName():
        useranme = config.get('Info', 'valid_username')
        return useranme

    @staticmethod
    def getPassword():
        password = config.get('Info', 'valid_password')
        return password

    @staticmethod
    def getInvalidUsername():
        invalid_username = config.get('Info', 'invalid_username')
        return invalid_username

    @staticmethod
    def getExp_Price():
        exp_price = config.get('Info', 'exp_price')
        return exp_price

    @staticmethod
    def getTotal_Exp_Price():
        exp_total_price = config.get('Info', 'exp_total_price')
        return exp_total_price

    @staticmethod
    def setValid_Email():
        valid_email = config.get('Info', 'valid_email')
        return valid_email

    @staticmethod
    def setValid_Email_Password():
        valid_email_password = config.get('Info', 'valid_email_password')
        return valid_email_password

    @staticmethod
    def setValid_Git_Password():
        valid_git_password = config.get('Info', 'valid_git_password')
        return valid_git_password

    @staticmethod
    def setInvalid_Email():
        invalid_email = config.get('Info', 'invalid_email')
        return invalid_email

    @staticmethod
    def setInvalid_Git_Password():
        invalid_git_password = config.get('Info', 'invalid_git_password')
        return invalid_git_password

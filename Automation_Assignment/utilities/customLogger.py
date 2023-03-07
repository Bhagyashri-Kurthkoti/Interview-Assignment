import datetime
import logging
import os

timestamp = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
log_file_path = os.path.abspath(os.path.join(os.getcwd(), "..", "Logs", f"automation_logs_{timestamp}.log"))


class SingletonLogger:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.logger = logging.getLogger(__name__)
            cls._instance.logger.setLevel(logging.INFO)
            handler = logging.FileHandler(log_file_path)
            handler.setLevel(logging.INFO)
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            handler.setFormatter(formatter)
            cls._instance.logger.addHandler(handler)
        return cls._instance

    def log_info(self, message):
        self.logger.info(message)

    def log_warning(self, message):
        self.logger.warning(message)

    def log_error(self, message):
        self.logger.error(message)

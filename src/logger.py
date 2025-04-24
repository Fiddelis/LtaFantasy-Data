import logging
import os
class LoggerSetup:
    def __init__(self, log_dir="logs", log_file="runtime.log", level=logging.INFO):
        self.log_dir = log_dir
        self.log_file = log_file
        self.level = level

    def setup(self):
        os.makedirs(self.log_dir, exist_ok=True)
        log_path = os.path.join(self.log_dir, self.log_file)

        logging.basicConfig(
            level=self.level,
            format="%(asctime)s [%(levelname)s] %(message)s",
            handlers=[
                logging.FileHandler(log_path),
                logging.StreamHandler()
            ]
        )
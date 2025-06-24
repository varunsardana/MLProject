import logging
import os
from datetime import datetime


base_dir = os.getcwd()
logs_dir = os.path.join(base_dir, "logs")
os.makedirs(logs_dir, exist_ok=True)


LOG_FILE = f"{datetime.now():%m_%d_%Y_%H_%M_%S}.log"
LOG_FILE_PATH = os.path.join(logs_dir, LOG_FILE)


logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)



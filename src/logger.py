import logging
import os
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(logs_path,exist_ok=True)

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)


LOGGING_LEVEL = logging.INFO
LOGGING_FORMAT = '%(asctime)s - %(levelname)s - Thread %(thread)d - %(filename)s - %(funcName)s() - line%(lineno)d::%(message)s'
DATE_FORMAT = '%m_%d_%Y %I_%M_%S %p'

logging.basicConfig(
    level=LOGGING_LEVEL,
    format=LOGGING_FORMAT, 
    datefmt=DATE_FORMAT,
    filename=LOG_FILE_PATH,
    
)
    


if __name__ == "__main__":
    logging.info("Logging has started")
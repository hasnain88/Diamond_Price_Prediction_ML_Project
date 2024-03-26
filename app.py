from src.logger import logging
from src.exception import CustomException




if __name__=="__main__":
    logging.info("Logging has started")
    try:
        a = 1/0
    except Exception as e:
        logging.info("Division by Zero")
        raise CustomException(e,sys)

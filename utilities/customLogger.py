import inspect
import logging


class LogGen:

    @staticmethod
    def getLogger():

        loggerName = inspect.stack()[1][3]
        logging.basicConfig(filename=".\\Logs\\automation.log",
                            format="%(asctime)s : %(levelname)s : %(name)s : %(message)s")

        logger = logging.getLogger(loggerName)
        logger.setLevel(logging.INFO)

        return logger


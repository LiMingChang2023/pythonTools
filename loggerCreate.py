import logging
import traceback
import sys

class Tracker():
    def __init__(self, name, mp=True):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.INFO)
        self.init_setting(name)

    def init_setting(self, name):
        handler = logging.FileHandler(f'{name}.log')
        format = logging.Formatter("[%(levelname)s] [%(name)s] [%(asctime)s], [line]: %(lineno)d [msg]: %(message)s")
        handler.setFormatter(format)
        self.logger.addHandler(handler)

    def exceptionInfo(self, terminate=False):
        _, exc_value, exc_traceback = sys.exc_info()
        tb = traceback.extract_tb(exc_traceback)[0]
        msg = f'[Error]: {exc_value} [file]: {tb[0]} [line]: {tb[1]}'

        if terminate:
            print(msg)
            raise Exception('process terminate')     
        return msg
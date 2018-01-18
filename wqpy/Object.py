from wqpy.static.constant import *
from logging import INFO
import time


class VtBaseData(object):
    def __init__(self, origin=EMPTY_STRING):
        self.origin = origin


class VtLogData(VtBaseData):
    def __init__(self, origin=EMPTY_STRING, log_level=INFO, log_content=EMPTY_UNICODE):
        super(VtLogData, self).__init__(origin)
        self.logTime = time.strftime('%X', time.localtime())
        self.logLevel = log_level
        self.logContent = log_content

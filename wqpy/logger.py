import logging
from datetime import datetime
from wqpy.helperFunc import get_temp_path


class Logger(object):
    # logging level, from low to high
    LEVEL_DEBUG = logging.DEBUG
    LEVEL_INFO = logging.INFO
    LEVEL_WARN = logging.WARNING
    LEVEL_ERROR = logging.ERROR
    LEVEL_CRITICAL = logging.CRITICAL

    instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.instance:
            cls.instance = super(Logger, cls).__new__(cls, *args, **kwargs)
        return cls.instance

    def __init__(self):
        self.logger = logging.getLogger()
        self.formatter = logging.Formatter('%(asctime)s  %(levelname)s: %(message)s')
        self.level = self.LEVEL_CRITICAL

        self.consoleHandler = None
        self.fileHandler = None

        null_handler = logging.NullHandler()
        self.logger.addHandler(null_handler)

        self.levelFunctionDict = {
            self.LEVEL_DEBUG: self.debug,
            self.LEVEL_INFO: self.info,
            self.LEVEL_WARN: self.warn,
            self.LEVEL_ERROR: self.error,
            self.LEVEL_CRITICAL: self.critical,
        }

    def set_level(self, level):
        self.logger.setLevel(level)
        self.level = level

    def add_console_handler(self):
        """添加终端输出"""
        if not self.consoleHandler:
            self.consoleHandler = logging.StreamHandler()
            self.consoleHandler.setLevel(self.level)
            self.consoleHandler.setFormatter(self.formatter)
            self.logger.addHandler(self.consoleHandler)

    def add_file_handler(self, filename=''):
        """添加文件输出"""
        if not self.fileHandler:
            if not filename:
                filename = 'vt_' + datetime.now().strftime('%Y%m%d') + '.log'
            file_path = get_temp_path(filename)
            self.fileHandler = logging.FileHandler(file_path)
            self.fileHandler.setLevel(self.level)
            self.fileHandler.setFormatter(self.formatter)
            self.logger.addHandler(self.fileHandler)

    def debug(self, msg):
        """开发时用"""
        self.logger.debug(msg)

    def info(self, msg):
        """正常输出"""
        self.logger.info(msg)

    def warn(self, msg):
        """警告信息"""
        self.logger.warning(msg)

    def error(self, msg):
        """报错输出"""
        self.logger.error(msg)

    def exception(self, msg):
        """报错输出+记录异常信息"""
        self.logger.exception(msg)

    def critical(self, msg):
        """影响程序运行的严重错误"""
        self.logger.critical(msg)

    def process_log_event(self, event):
        """处理日志事件"""
        log = event.dict_['data']
        log_func = self.levelFunctionDict[log.logLevel]     # 获取日志级别对应的处理函数
        msg = '\t'.join([log.origin, log.logContent])
        log_func(msg)

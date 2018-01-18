from collections import OrderedDict
from .eventEngine import EventEngine, Event
from .logger import Logger
from .helperFunc import get_global_setting
from wqpy.static.eventType import *
from .Object import *


class MainEngine(object):
    def __init__(self):
        self.globalSetting = {}
        self.load_setting()

        self.__appDict = OrderedDict()
        self.__mdDict = OrderedDict()
        self.__tdDict = OrderedDict()

        self.eventEngine = EventEngine()
        self.eventEngine.start()

        self.logger = Logger()
        self.init_logger()

    def load_setting(self):
        self.globalSetting = get_global_setting()

    def add_app(self, app_engine):
        app_obj = app_engine(self, self.eventEngine)
        app_name = app_obj.appName
        self.__appDict[app_name] = app_obj
        self.write_log("add App "+app_name+" success")

    def get_app(self, app_name):
        return self.__appDict[app_name]

    def add_md_api(self, md_api):
        md_api_obj = md_api(self.eventEngine)
        md_api_name = md_api_obj.mdName
        self.__tdDict[md_api_name] = md_api_obj
        self.write_log("add market data api " + md_api_name + " success")

    def connect_md(self, md_name):
        pass

    def get_md_api(self, md_name):
        return self.__mdDict[md_name]

    def add_td_api(self, td_api):
        td_api_obj = td_api(self.eventEngine)
        td_api_name = td_api_obj.tdName
        self.__tdDict[td_api_name] = td_api_obj
        self.write_log("add Trader api " + td_api_name + " success")

    def connect_td(self, td_name):
        pass

    def get_td_api(self, td_name):
        return self.__mdDict[td_name]

    def send_order(self, order_req, td_name):
        pass

    def cancel_order(self, cancel_order_req, td_name):
        pass

    def qry_account(self, td_name):
        pass

    def qry_position(self, td_name):
        pass

    def subscribe(self, subscribe_req, md_name):
        pass

    def init_logger(self):
        """初始化日志引擎"""
        if not self.globalSetting["logActive"]:
            return

        # 设置日志级别
        level_dict = {
            "debug": self.logger.LEVEL_DEBUG,
            "info": self.logger.LEVEL_INFO,
            "warn": self.logger.LEVEL_WARN,
            "error": self.logger.LEVEL_ERROR,
            "critical": self.logger.LEVEL_CRITICAL,
        }
        level = level_dict.get(self.globalSetting["logLevel"], self.logger.LEVEL_CRITICAL)
        self.logger.set_level(level)

        # 设置输出
        if self.globalSetting['logConsole']:
            self.logger.add_console_handler()

        if self.globalSetting['logFile']:
            self.logger.add_file_handler()

        # 注册事件监听
        self.eventEngine.register(EVENT_LOG, self.logger.process_log_event)

    def write_log(self, content):
        log_data = VtLogData("MainEngine", INFO, content)
        event = Event(EVENT_LOG)
        event.dict_['data'] = log_data
        self.eventEngine.put(event)

    def exit(self, sleep_time=0):
        time.sleep(sleep_time)
        for td_api in self.__tdDict.values():
            td_api.close()

        for md_api in self.__mdDict.values():
            md_api.close()

        for app in self.__appDict.values():
            app.stop()

        self.eventEngine.stop()
        self.write_log("exit")

from collections import OrderedDict
from .eventEngine import EventEngine


class MainEngine(object):
    def __init__(self):
        self.__appDict = OrderedDict()
        self.__mdDict = OrderedDict()
        self.__tdDict = OrderedDict()

        self.__eventEngine = EventEngine()
        self.__eventEngine.start()

    def add_app(self, app_engine):
        app_name = app_engine.app_name
        self.__appDict[app_name] = app_engine(self, self.__eventEngine)

    def get_app(self, app_name):
        pass

    def add_md_api(self, md_api):
        md_api_name = md_api.md_name
        self.__tdDict[md_api_name] = md_api(self.__eventEngine)

    def connect_md(self, md_name):
        pass

    def get_md_api(self, md_name):
        pass

    def add_td_api(self, td_api):
        td_api_name = td_api.td_name
        self.__tdDict[td_api_name] = td_api(self.__eventEngine)

    def connect_td(self, td_name):
        pass

    def get_td_api(self, td_name):
        pass

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

    def exit(self):
        pass

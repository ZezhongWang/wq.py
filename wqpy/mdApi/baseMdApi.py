
class BaseMdApi(object):
    def __init__(self, event_engine, md_name):
        self.__md_name = md_name
        self.__event_engine = event_engine

    def login(self):
        pass

    def close(self):
        pass

    def subscribe(self, subscribe_req):
        pass

    def on_tick(self, tick):
        pass

    def on_contract(self, contract):
        pass











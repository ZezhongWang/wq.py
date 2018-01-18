from .baseMdApi import BaseMdApi


class SimulateMdApi(BaseMdApi):
    def __init__(self, event_engine, md_name='SimulateMdApi'):
        super(SimulateMdApi, self).__init__(event_engine, md_name)

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











from wqpy.tdApi.baseTdApi import BaseTdApi


class CtpTdApi(BaseTdApi):
    def __init__(self, event_engine):
        super(CtpTdApi, self).__init__(event_engine, td_name='CtpTdApi')

    def connect(self):
        pass

    def send_order(self, order_req):
        # refactor order_req into dict
        # and call the function in c++ ( unresolved , how to ?)
        pass




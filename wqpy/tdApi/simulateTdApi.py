from wqpy.tdApi.baseTdApi import BaseTdApi


class SimulateTdApi(BaseTdApi):
    def __init__(self, event_engine, td_name='Simulate'):
        super(SimulateTdApi, self).__init__(event_engine, td_name)

    def connect(self):
        pass

    def send_order(self, order_req):
        # refactor order_req into dict
        # and call the function in c++ ( unresolved , how to ?)
        pass

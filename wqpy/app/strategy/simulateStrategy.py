from .baseStrategy import BaseStrategy


class SimulateStrategy(BaseStrategy):
    def __init__(self, strategy_engine, strategy_name='SimulateStrategy'):
        super(SimulateStrategy, self).__init__(strategy_engine, strategy_name)

    def on_init(self):
        pass

    def on_start(self):
        pass

    def on_stop(self):
        pass

    def on_tick(self, tick):
        pass

    def on_order(self, order):
        pass

    def on_trade(self, trade):
        pass

    def on_finish(self, finish):
        pass

    def subscribe(self, subscribe_req):
        pass

    def on_contract(self, contract):
        pass

    def send_order(self, order_req):
        pass

    def cancel_order(self, cancel_order_req):
        pass

    def qry_account(self):
        pass

    def qry_position(self):
        pass

from .baseStrategy import BaseStrategy


class FirstStrategy(BaseStrategy):
    def __init__(self, strategy_engine, strategy_name='FirstStrategy'):
        super(FirstStrategy, self).__init__(strategy_engine, strategy_name)

    def on_tick(self, tick):
        pass

    def on_order(self, order):
        pass

    def on_trade(self, trade):
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

from wqpy.app.strategy.strategyEngine import StrategyEngine


class BaseStrategy(object):
    def __init__(self, strategy_engine, strategy_name):
        self.strategyName = strategy_name
        self.__strategyEngine = strategy_engine

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

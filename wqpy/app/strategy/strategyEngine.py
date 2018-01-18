from wqpy.app.baseAppEngine import BaseAppEngine
from wqpy.static.eventType import *
from wqpy.app.strategy.simulateStrategy import SimulateStrategy


class StrategyEngine(BaseAppEngine):
    def __init__(self, main_engine, event_engine, app_name='Strategy'):
        super(StrategyEngine, self).__init__(main_engine, event_engine, app_name)
        self.__strategyDict = {}
        self.__tickStrategyDict = {}

    def __run(self):
        self.load_strategy()
        self.init_all()
        self.start_all()

    def start(self):
        self.active = True
        self.thread.start()
        self.__run()

    def register_event(self):
        self.eventEngine.register(EVENT_TICK, self.process_tick_event)
        self.eventEngine.register(EVENT_ORDER, self.process_order_event)
        self.eventEngine.register(EVENT_TRADE, self.process_trade_event)
        self.eventEngine.register(EVENT_FINISH, self.process_trade_event)

    def stop(self):
        self.active = False
        self.thread.join()

    def process_tick_event(self, event):
        tick = event.dict_['data']
        # self.processStopOrder(tick)
        if tick.vtSymbol in self.__tickStrategyDict:
            strategy_list = self.__tickStrategyDict[tick.vtSymbol]
            for strategy in strategy_list:
                strategy.onTick(tick)

    def process_order_event(self, event):
        order = event.dict_['data']
        # self.processStopOrder(tick)
        if order.vtSymbol in self.__tickStrategyDict:
            strategy_list = self.__tickStrategyDict[order.vtSymbol]
            for strategy in strategy_list:
                strategy.onOrder(order)

    def process_trade_event(self, event):
        trade = event.dict_['data']
        # self.processStopOrder(tick)
        if trade.vtSymbol in self.__tickStrategyDict:
            strategy_list = self.__tickStrategyDict[trade.vtSymbol]
            for strategy in strategy_list:
                strategy.onTrade(trade)

    def process_finish_event(self, event):
        finish = event.dict_['data']
        # self.processStopOrder(tick)
        if finish.vtSymbol in self.__tickStrategyDict:
            strategy_list = self.__tickStrategyDict[finish.vtSymbol]
            for strategy in strategy_list:
                strategy.onFinish(finish)

    def load_strategy(self):
        strategy = SimulateStrategy(self)
        self.__strategyDict[strategy.strategyName] = strategy

    def init_strategy(self, strategy_name):
        strategy = self.__strategyDict[strategy_name]
        strategy.on_init()

    def start_strategy(self, strategy_name):
        strategy = self.__strategyDict[strategy_name]
        strategy.on_start()

    def stop_strategy(self, strategy_name):
        strategy = self.__strategyDict[strategy_name]
        strategy.on_stop()

    def remove_strategy(self, strategy_name):
        if strategy_name in self.__strategyDict:
            del self.__strategyDict[strategy_name]
        else:
            pass

    def init_all(self):
        for strategy_name in self.__strategyDict.keys():
            self.init_strategy(strategy_name)

    def start_all(self):
        for strategy_name in self.__strategyDict.keys():
            self.start_strategy(strategy_name)

    def stop_all(self):
        for strategy_name in self.__strategyDict.keys():
            self.stop_strategy(strategy_name)

    def clear(self):
        self.__strategyDict.clear()

    def send_order(self, order_req):
        pass

    def cancel_order(self, order_req):
        pass

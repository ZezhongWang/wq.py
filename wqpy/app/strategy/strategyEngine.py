from wqpy.app.baseAppEngine import BaseAppEngine
from wqpy.static.eventType import *
from threading import Thread
from datetime import datetime, timedelta


class StrategyEngine(BaseAppEngine):
    def __init__(self, main_engine, event_engine, app_name='Strategy'):
        super(StrategyEngine, self).__init__(main_engine, event_engine, app_name)
        self.__strategyDict = {}
        self.__tickStrategyDict = {}

    def __run(self):
        pass

    def start(self):
        self.__active = True
        self.__thread.start()
        self.__run()

    def register_event(self):
        self.__eventEngine.register(EVENT_TICK, self.process_tick_event)
        self.__eventEngine.register(EVENT_ORDER, self.process_order_event)
        self.__eventEngine.register(EVENT_TRADE, self.process_trade_event)
        self.__eventEngine.register(EVENT_FINISH, self.process_trade_event)

    def stop(self):
        self.__active = False
        self.__thread.join()

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

    def load_strategy(self, trade):
        pass

    def send_order(self, order_req):
        pass

    def cancel_order(self, order_req):
        pass

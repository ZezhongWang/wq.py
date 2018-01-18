from wqpy.eventEngine import Event
from wqpy.static.eventType import *


class BaseTdApi(object):
    # base trader api function's parameters is consistent
    def __init__(self, event_engine, td_name):
        self.td_name = td_name
        self.__event_engine = event_engine

        self.connection_status = False
        self.login_status = False

        self.__reqID = 0
        self.__orderRef = 0

        self.__fileName = self.td_name + '_connect.json'

    # realize in base class
    def on_order(self, order):
        """order change"""
        # general event
        event1 = Event(type_=EVENT_ORDER)
        event1.dict_['data'] = order
        self.__event_engine.put(event1)

        # specific order event
        event2 = Event(type_=EVENT_ORDER + order.vtOrderID)
        event2.dict_['data'] = order
        self.__event_engine.put(event2)

    def on_trade(self, trade):
        # general event
        event1 = Event(type_=EVENT_TRADE)
        event1.dict_['data'] = trade
        self.__event_engine.put(event1)

        # specific order event
        event2 = Event(type_=EVENT_TRADE+ trade.vtTradeID)
        event2.dict_['data'] = trade
        self.__event_engine.put(event2)

    def on_position(self, position):
        # general event
        event1 = Event(type_=EVENT_POSITION)
        event1.dict_['data'] = position
        self.__event_engine.put(event1)

        # specific order event
        event2 = Event(type_=EVENT_POSITION + position.vtSymbol)
        event2.dict_['data'] = position
        self.__event_engine.put(event2)

    def on_account(self, account):
        # general event
        event1 = Event(type_=EVENT_ACCOUNT)
        event1.dict_['data'] = account
        self.__event_engine.put(event1)

        # specific order event
        event2 = Event(type_=EVENT_ACCOUNT + account.vtAccountID)
        event2.dict_['data'] = account
        self.__event_engine.put(event2)

    def on_contract(self, contract):
        # general event
        event1 = Event(type_=EVENT_CONTRACT)
        event1.dict_['data'] = contract
        self.__event_engine.put(event1)

    # request and query realize in subclass
    def login(self):
        pass

    def close(self):
        pass

    def send_order(self, order_req):
        pass

    def cancel_order(self, cancel_order_req):
        pass

    def qry_account(self):
        pass

    def qry_position(self):
        pass

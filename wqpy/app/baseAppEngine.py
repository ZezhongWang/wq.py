from queue import Queue, Empty
from threading import Thread
from collections import defaultdict


class BaseAppEngine(object):
    def __init__(self, main_engine, event_engine, app_name):
        self.appName = app_name
        self.__mainEngine = main_engine
        self.__eventEngine = event_engine
        self.__thread = Thread(target=self.__run)
        self.__active = False
        self.register_event()

    def __run(self):
        pass

    def start(self):
        self.__active = True
        self.__thread.start()
        self.__run()

    def register_event(self):
        pass

    def stop(self):
        self.__active = False
        self.__thread.join()



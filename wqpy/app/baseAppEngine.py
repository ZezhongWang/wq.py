from queue import Queue, Empty
from threading import Thread
from collections import defaultdict


class BaseAppEngine(object):
    def __init__(self, main_engine, event_engine, app_name):
        self.appName = app_name
        self.mainEngine = main_engine
        self.eventEngine = event_engine
        self.thread = Thread(target=self.__run)
        self.active = False
        self.register_event()

    def __run(self):
        pass

    def start(self):
        self.active = True
        self.thread.start()
        self.__run()

    def register_event(self):
        pass

    def stop(self):
        self.active = False
        self.thread.join()



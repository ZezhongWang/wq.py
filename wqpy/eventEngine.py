from queue import Queue, Empty
from threading import Thread
from collections import defaultdict


class Event(object):
    def __init__(self, type_=None):
        self.type_ = type_
        self.dict_ = {}


class EventEngine(object):
    def __init__(self):
        self.__queue = Queue()
        self.__active = False
        self.__thread = Thread(target=self.__run)
        self.__handlers = defaultdict(list)
        self.__generalHandlers = []

    def __run(self):
        while self.__active:
            try:
                event = self.__queue.get(block=True, timeout=1)
                self.__process(event)
            except Empty:
                pass

    def __process(self, event):
        if event.type_ in self.__handlers:
            [handler(event) for handler in self.__handlers[event.type_]]

        if event.type_ in self.__generalHandlers:
            [handler(event) for handler in self.__generalHandlers[event.type_]]

    def start(self):
        self.__active = True
        self.__thread.start()
        self.__run()

    def stop(self):
        self.__active = False
        self.__thread.join()

    def register(self, type_, handler):
        handler_list = self.__handlers[type_]
        if handler not in handler_list:
            handler_list.append(handler)

    def unregister(self, type_, handler):
        handler_list = self.__handlers[type_]
        if handler in handler_list:
            handler_list.remove(handler)
        if not handler_list:
            del self.__handlers[type_]

    def put(self, event):
        self.__queue.put(event)

    def register_general_handler(self, handler):
        if handler not in self.__generalHandlers:
            self.__generalHandlers.append(handler)

    def unregister_general_handler(self, handler):
        if handler in self.__generalHandlers:
            self.__generalHandlers.remove(handler)
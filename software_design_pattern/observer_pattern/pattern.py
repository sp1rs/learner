"""Example to understand observer pattern. It is a behavioural pattern."""

"""
Just a skeleton code for now.
"""


from abc import ABCMeta

class ObservableInterface(metaclass=ABCMeta):

    def add(self, observer):
        pass

    def remove(self, observer):
        pass

    def notify(self):
        pass


class Observable(ObservableInterface):

    def __init__(self, *args, **kwargs):
        self._observers = []

    def add(self, observer):
        self._observers.append(observer)

    def remove(self, observer):
        self._observers.remove(observer)

    def notify(self):
        for observer in self._observers:
            observer.update()

    def get_info(self):
        pass

class ObserverInterface(metaclass=ABCMeta):
    def update(self):
        pass


class Observer1(ObservableInterface):

    def __init__(self, observerable):
        self.observerable = observerable

    def update(self):
        self.observerable.get_info()


class Observer2(ObservableInterface):

    def __init__(self, observerable):
        self.observerable = observerable

    def update(self):
        self.observerable.get_info()


# Code flow.

observerable = Observable()
observer1 = Observer1(observerable)
observer2 = Observer1(observerable)
observerable.add(observer1)
observerable.add(observer2)

observerable.notify()

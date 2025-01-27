import time
# clock
# log file
# heavy

# 1 - static
# 2 - Singleton

# the object will be created only once upon demand (=lazy initialization)
# class which could be initiated only 1 time
# cannot create objects with __init__
# getting an object will always return the same object
# cannot delete the object and create a new one

from datetime import datetime

class TimerSingleton:

    __instance = None  # will keep the object

    def __init__(self):
        raise RuntimeError("cannot create objects in Singleton")

    @classmethod
    def get_instance(cls):
        if not cls.__instance:
            cls.__instance = object.__new__(cls)

            # data, this will be different between classes
            cls.__instance.__start_time = datetime.now()

        return cls.__instance

    def get_time(self):
        return datetime.now() - self.__start_time

TimerSingleton.get_instance()
print(TimerSingleton.get_instance().get_time())

# s1 = TimerSingleton()  # Error
s1 = TimerSingleton.get_instance()
s2 = TimerSingleton.get_instance()
s2.radius = 4.5
print(s1 == s2)
time.sleep(1 / 2)
print(s1.get_time())
print(type(s1))
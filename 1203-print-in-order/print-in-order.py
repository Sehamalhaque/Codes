import threading

class Foo:
    def __init__(self):
        self.first_done = threading.Event()
        self.second_done = threading.Event()

    def first(self, printFirst: 'Callable[[], None]') -> None:
        printFirst()
        self.first_done.set()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        self.first_done.wait()
        printSecond()
        self.second_done.set()

    def third(self, printThird: 'Callable[[], None]') -> None:
        self.second_done.wait()
        printThird()

def printFirst(): print("first", end="")
def printSecond(): print("second", end="")
def printThird(): print("third", end="")

foo = Foo()

from threading import Thread

threads = [
    Thread(target=foo.third, args=(printThird,)),
    Thread(target=foo.second, args=(printSecond,)),
    Thread(target=foo.first, args=(printFirst,))
]

for t in threads:
    t.start()
for t in threads:
    t.join()

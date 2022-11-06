class Observer:

    def __init__(self, observable):
        observable.subscribe(self)

    def update(self, msg: str):
        print(msg)


class Observable:

    def __init__(self):
        self.observers: list[Observer] = []

    def subscribe(self, observalble: Observer):
        self.observers.append(observalble)

    def update(self, msg):
        [o.update(msg) for o in self.observers]


if __name__=='__main__':
    o1 = Observable()
    Observer(o1)
    Observer(o1)
    o1.update('hi all observers!')

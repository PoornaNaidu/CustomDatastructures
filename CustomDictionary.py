referValues = {None: 0, int: 0, float: 0.0, str: 'NaN', list: list(), dict: dict(), set: set()}


class CustomDictionary(dict):

    def __init__(self, setValueType=None):
        self.setValueType = setValueType

    def __getitem__(self, key):
        self.setdefault(key, referValues[self.setValueType])
        return dict.__getitem__(self, key)


class Counter(CustomDictionary):

    def __init__(self,d = None, type=int):
        if type is int:
            self.setValueType = int
        elif type is float:
            self.setValueType = float
        else:
            print("Only integer and float values allowed.\nDefault value 'int' set.")
            self.setValueType = int

        if d is not None:
            for key in d.keys():
                self[key] = d[key]


    def append(self, d):
        if type(d) is dict:
            for key in d.keys():
                self.setdefault(key, d[key])
        else:
            self.setdefault(d, referValues[self.setValueType])

    def increment(self,keys = None,value = 1):
        if keys is None:
            keys = self.keys()

        for key in keys:
            self[key] += value

    def decrement(self,keys = None,value = 1):
        if keys is None:
            keys = self.keys()

        for key in keys:
            self[key] -= value

    def multiply(self,keys = None,value = 1):
        if keys is None:
            keys = self.keys()

        for key in keys:
            self[key] *= value

    def divide(self,keys = None,value = 1):
        if keys is None:
            keys = self.keys()

        if value == 0:
            raise ZeroDivisionError
        else:
            for key in keys:
                self[key] /= value

    def argMax(self):

        if len(self) == 0:
            return None
        else:
            items = list(self.items())
            values = [x[1] for x in items]
            maxIndex = values.index(max(values))
            return items[maxIndex][0]

    def __add__(self, y):
        newCounter = Counter()
        for key in self:
            if key in y:
                newCounter[key] = self[key] + y[key]
            else:
                newCounter[key] = self[key]
        for key in y:
            if key in self:
                continue
            newCounter[key] = y[key]
        return newCounter

    def __sub__(self, y):
        newCounter = Counter()
        for key in self:
            if key in y:
                newCounter[key] = self[key] - y[key]
            else:
                newCounter[key] = self[key]

        return newCounter
referValues = {None: 0, int: 0, float: 0.0, str: 'NaN', list: list(), dict: dict(), set: set()}


class CustomDictionary(dict):

    def __init__(self, setValueType=None):
        self.setValueType = setValueType

    def __getitem__(self, key):
        self.setdefault(key, referValues[self.setValueType])
        return dict.__getitem__(self, key)


class Counter(CustomDictionary):

    def __init__(self, type=int):
        if type is int:
            self.setValueType = int
        elif type is float:
            self.setValueType = float
        else:
            print("Only integer and float values allowed.\nDefault value 'int' set.")
            self.setValueType = int


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


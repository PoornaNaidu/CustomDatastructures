referValues = {None : 0, int: 0, float: 0.0, str: 'NaN', list: list(),dict : dict(), set: set()}

class CustomDictionary(dict):

    def __init__(self,setValueType = None):
        self.setValueType = setValueType

    def __getitem__(self, key):
        self.setdefault(key,referValues[self.setValueType])
        return dict.__getitem__(self, key)


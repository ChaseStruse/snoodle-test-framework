def expect(value):
    return Expectation(value)

class Expectation:
    def __init__(self, value):
        self.value = value

    def toEqual(self, comparison):
        print(f'expecting {self.value} to equal {comparison}')
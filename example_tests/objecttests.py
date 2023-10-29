from snoodle_test.expectations import expect


class TClass:
    def __init__(self, attr):
        self.attr = attr


class TestObjects:
    def test_is_the_same_success(self):
        test = TClass(attr="test")
        expect(test).is_the_same(test)

    def test_is_the_same_fails(self):
        test = TClass(attr="test")
        other_test = TClass(attr="other test")
        expect(test).is_the_same(other_test)

    def test_is_not_the_same_success(self):
        test = TClass(attr="test")
        other_test = TClass(attr="other test")
        expect(test).is_not_the_same(other_test)

    def test_is_not_the_same_fails(self):
        test = TClass(attr="test")
        expect(test).is_not_the_same(test)

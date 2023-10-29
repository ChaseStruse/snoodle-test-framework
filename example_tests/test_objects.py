from snoodle_test.expectations import *


class TClass:
    def __init__(self, attr):
        self.attr = attr


class TestObjects:
    def test_is_the_same_success(self):
        test = TClass(attr="test")
        ObjectsAreTheSame(actual=test, expected=test)

    def test_is_the_same_fails(self):
        test = TClass(attr="test")
        other_test = TClass(attr="other test")
        ObjectsAreTheSame(actual=test, expected=other_test)

    def test_is_not_the_same_success(self):
        test = TClass(attr="test")
        other_test = TClass(attr="other test")
        ObjectsAreNotTheSame(actual=test, expected=other_test)

    def test_is_not_the_same_fails(self):
        test = TClass(attr="test")
        ObjectsAreNotTheSame(actual=test, expected=test)

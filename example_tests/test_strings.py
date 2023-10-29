from snoodle_test.expectations import expect
from snoodle_test.expectations import *


class TestStrings:

    def test_string_success(self):
        IsEqual(actual="hello", expected="hello")

    def test_string_failure(self):
        IsEqual(actual="hello", expected="hi")

import dataclasses
from snoodle_test.expectations import *


class TestNumbers:

    def test_is_equal_success(self):
        IsEqual(actual=10, expected=10)

    def test_is_equal_fails(self):
        IsEqual(actual=10, expected=5)

    def test_is_not_equal_success(self):
        IsNotEqual(actual=10, expected=5)

    def test_is_not_equal_fails(self):
        IsNotEqual(actual=10, expected=10)

    def test_is_less_than_success(self):
        IsLessThan(actual=5, expected=10)

    def test_is_less_than_fails(self):
        IsLessThan(actual=10, expected=5)

    def test_is_greater_than_success(self):
        IsGreaterThan(actual=10, expected=5)

    def test_num_greater_than_fails(self):
        IsGreaterThan(actual=5, expected=10)

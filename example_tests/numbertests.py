import dataclasses
from snoodle_test.expectations import expect


class TestNumbers:

    def test_num_success(self):
        expect(1 + 1).is_equal(2)

    def test_num_failure(self):
        expect(1 + 1).is_equal(22)

    def test_num_less_than(self):
        expect(25).is_less_than(28)

    def test_num_greater_than(self):
        expect(25).is_greater_than(10)

    def test_num_less_than_fails(self):
        expect(25).is_less_than(1)

    def test_num_greater_than_fails(self):
        expect(25).is_greater_than(100)

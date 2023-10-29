import dataclasses
from snoodle_test.expectations import expect


@dataclasses.dataclass
class TClass:
    def __init__(self, name):
        self.name = name

    name: str


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

    def test_objects(self):
        test = TClass(name="test")
        expect(test).is_the_same(test)

    def test_object_comparison_failing(self):
        test = TClass(name="test")
        other_test = TClass(name="other test")
        expect(test).is_the_same(other_test)

import operator


def expect(value):
    return Expectation(value)


def get_operator_string_value(op):
    """
    Gets the string value of a standard operator and converts it to a printable value.
    :param op:
    :return:
    """
    if op == operator.eq:
        return "to equal"
    if op == operator.is_not:
        return "not to equal"
    if op == operator.lt:
        return "to be less than"
    if op == operator.gt:
        return "to be greater than"
    if op == operator.is_:
        return "to be the same as"


class FailedExpectation(RuntimeError):
    """
    Custom exception that will return a custom error message.
    """
    def __init__(self, message):
        self.message = message


class Expectation:
    """
    This class is to be used within the test files to evaluate assertions.
    :param value: value that you would like to compare
    """
    def __init__(self, value):
        self.value = value

    def is_equal(self, comparison: str) -> bool:
        """
        Checks if the values are equal by invoking the _assert method\n
        :param comparison: The value that is to be evaluated
        :return: True, unless it is failing then it will raise an error and not return. These errors are handled within
                 the runner.py
        """
        return self._assert(comparison, operator.eq)

    def is_not_equal(self, comparison: str) -> bool:
        """
        Checks if the values are not equal by invoking the _assert method\n
        :param comparison: The value that is to be evaluated
        :return: True, unless it is failing then it will raise an error and not return. These errors are handled within
                 the runner.py
        """
        return self._assert(comparison, operator.is_not)

    def is_less_than(self, comparison: str) -> bool:
        """
        Checks if the value is less than by invoking the _assert method\n
        :param comparison: The value that is to be evaluated
        :return: True, unless it is failing then it will raise an error and not return. These errors are handled within
                 the runner.py
        """
        return self._assert(comparison, operator.lt)

    def is_greater_than(self, comparison: str) -> bool:
        """
        Checks if the value is greater than by invoking the _assert method\n
        :param comparison: The value that is to be evaluated
        :return: True, unless it is failing then it will raise an error and not return. These errors are handled within
                 the runner.py
        """
        return self._assert(comparison, operator.gt)

    def is_the_same(self, comparison) -> bool:
        return self._assert(comparison, operator.is_)

    def _assert(self, comparison, oper: operator) -> bool:
        """
        Checks if the given test is failing\n
        :param comparison: The value that is to be evaluated
        :param oper: operator from the Operator library
        :return: True
        """
        if not oper(self.value, comparison):
            raise FailedExpectation(f"Expected {self.value} {get_operator_string_value(oper)} {comparison}")

        return True




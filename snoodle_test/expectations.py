import operator


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


class IsEqual(Expectation):
    def __init__(self, actual, expected):
        super().__init__(actual)
        self.expected = expected
        self.is_equal(expected)

    def is_equal(self, comparison: str) -> bool:
        """
        Checks if the values are equal by invoking the _assert method\n
        :param comparison: The value that is to be evaluated
        :return: True, unless it is failing then it will raise an error and not return. These errors are handled within
                 the runner.py
        """
        return self._assert(comparison, operator.eq)


class IsNotEqual(Expectation):
    def __init__(self, actual, expected):
        super().__init__(actual)
        self.expected = expected
        self.is_not_equal(expected)

    def is_not_equal(self, comparison: str) -> bool:
        """
        Checks if the values are not equal by invoking the _assert method\n
        :param comparison: The value that is to be evaluated
        :return: True, unless it is failing then it will raise an error and not return. These errors are handled within
                 the runner.py
        """
        return self._assert(comparison, operator.ne)


class IsLessThan(Expectation):
    def __init__(self, actual, expected):
        super().__init__(actual)
        self.expected = expected
        self.is_less_than(expected)

    def is_less_than(self, comparison: str) -> bool:
        """
        Checks if the value is less than by invoking the _assert method\n
        :param comparison: The value that is to be evaluated
        :return: True, unless it is failing then it will raise an error and not return. These errors are handled within
                 the runner.py
        """
        return self._assert(comparison, operator.lt)


class IsGreaterThan(Expectation):
    def __init__(self, actual, expected):
        super().__init__(actual)
        self.expected = expected
        self.is_greater_than(expected)

    def is_greater_than(self, comparison: str) -> bool:
        """
        Checks if the value is greater than by invoking the _assert method\n
        :param comparison: The value that is to be evaluated
        :return: True, unless it is failing then it will raise an error and not return. These errors are handled within
                 the runner.py
        """
        return self._assert(comparison, operator.gt)


class ObjectsAreTheSame(Expectation):
    def __init__(self, actual, expected):
        super().__init__(actual)
        self.expected = expected
        self.is_the_same(expected)

    def is_the_same(self, comparison) -> bool:
        """
        Checks if the object is the same by invoking the _assert method\n
        :param comparison: The value that is to be evaluated
        :return: True, unless it is failing then it will raise an error and not return. These errors are handled within
                 the runner.py
        """
        return self._assert(comparison, operator.is_)


class ObjectsAreNotTheSame(Expectation):
    def __init__(self, actual, expected):
        super().__init__(actual)
        self.expected = expected
        self.is_not_the_same(expected)

    def is_not_the_same(self, comparison) -> bool:
        """
        Checks if the object is not the same by invoking the _assert method\n
        :param comparison: The value that is to be evaluated
        :return: True, unless it is failing then it will raise an error and not return. These errors are handled within
                 the runner.py
        """
        return self._assert(comparison, operator.is_not)


def get_operator_string_value(op: operator) -> str:
    """
    Gets the string value of a standard operator and converts it to a printable value.
    :param op: operator that is being used, for example operator.eq
    :return: str value that equates to the operator
    """
    operator_str_values = {
        operator.eq: "equal to",
        operator.ne: "not to equal",
        operator.lt: "to be less than",
        operator.gt: "to be greater than",
        operator.is_: "to be the same as",
        operator.is_not: "to not be the same as"
    }
    return operator_str_values[op]


def expect(value) -> Expectation:
    """Creates an expectation obj that will then be used to create comparisons"""
    return Expectation(value)

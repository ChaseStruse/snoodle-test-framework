from snoodle_test.expectations import expect


class TestStrings:

    def test_string_success(self):
        expect('Hello').is_equal('Hello')

    def test_string_failure(self):
        expect('hello').is_equal('hi')

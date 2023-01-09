from src.expectations import expect

class TestStrings:

    def test_string_success(self):
        expect('Hello').toEqual('Hello')


    def test_string_failure(self):
        expect('hello').toEqual('hi')

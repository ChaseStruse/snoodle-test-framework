from snoodle_test.expectations import expect


class TestBooleans:
    def test_success(self):
        expect(True).toEqual(True)

    def test_failure(self):
        expect(False).toEqual(True)

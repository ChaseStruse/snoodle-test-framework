from snoodle_test.expectations import expect


class TestBooleans:
    def test_success(self):
        expect(True).is_equal(True)

    def test_failure(self):
        expect(False).is_equal(True)

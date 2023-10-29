from snoodle_test.expectations import expect


class TestNumbers:

    def test_num_success(self):
        expect(1 + 1).is_equal(2)

    def test_num_failure(self):
        expect(1 + 1).is_equal(22)

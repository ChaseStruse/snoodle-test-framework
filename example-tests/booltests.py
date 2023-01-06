from src.expectations import expect


def test_success():
    expect(True).toEqual(True)


def test_failure():
    expect(False).toEqual(False)

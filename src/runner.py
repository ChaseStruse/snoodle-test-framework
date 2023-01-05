import booltests
from inspect import getmembers, isfunction

tests = [m for m in getmembers(booltests) if isfunction(m[1]) and m[0].startswith('test_')]


def run():
    success = True
    for test in tests:
        (test_name, test_function) = test
        try:
            test_function()
            print(f'running test {test_name} - success')
        except AssertionError:
            print(f'running test {test_name} - failure')
            success = False

    if success:
        print(f'test succeeded')
    else:
        print(f'test failed')


if __name__ == '__main__':
    run()
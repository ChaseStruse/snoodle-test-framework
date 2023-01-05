import importlib.machinery
import sys
import types
from inspect import getmembers, isfunction

def load_tests(mod):
    return [m for m in getmembers(mod) if isfunction(m[1]) and m[0].startswith('test_')]

def load_module(file):
    loader = importlib.machinery.SourceFileLoader('testmod', file)
    mod = types.ModuleType('testmod')
    loader.exec_module(mod)
    return mod

def run(file):
    mod = load_module(file)
    tests = load_tests(mod)
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
    run(sys.argv[1])

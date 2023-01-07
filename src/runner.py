import importlib.machinery
import sys
import types
from inspect import getmembers, isfunction
import os
import colors
import expectations


class Runner:
    def __init__(self, path):
        self.test_files = []
        self.success = True
        self.load_test_files(path)

    def load_test_files(self, path):
        if path.endswith('__pycache__'):
            return
        if os.path.isfile(path):
            self.test_files.append(path)
        elif os.path.isdir(path):
            for nested_path in os.listdir(path):
                self.load_test_files(path + '/' + nested_path)

    @staticmethod
    def load_tests(mod):
        return [m for m in getmembers(mod) if isfunction(m[1]) and m[0].startswith('test_')]

    @staticmethod
    def load_module(file):
        loader = importlib.machinery.SourceFileLoader('testmod', file)
        mod = types.ModuleType('testmod')
        loader.exec_module(mod)
        return mod

    def run_single_file(self, file):
        mod = self.load_module(file)
        tests = self.load_tests(mod)
        for test in tests:
            (test_name, test_function) = test
            try:
                test_function()
                print(f'running test {test_name} - {colors.GREEN}success{colors.RESET}')
            except expectations.FailedExpectation as e:
                print(f'running test {test_name} - {colors.RED}failure{colors.RESET}')
                self.success = False

    def run(self):
        for test_file in self.test_files:
            self.run_single_file(test_file)
        if self.success:
            print(f'{colors.GREEN}test succeeded{colors.RESET}')
        else:
            print(f'{colors.RED}test failed{colors.RESET}')


def main():
    Runner(sys.argv[1]).run()

import importlib.machinery
import sys
import types
from inspect import getmembers, isclass
import os
from snoodle_test.colors import RED, GREEN, RESET
from snoodle_test.expectations import FailedExpectation


class Runner:
    def __init__(self, path):
        self.files = []
        self.successes, self.failures = 0, 0
        self.find_test_files(path)
        self.failingFiles = []

    @staticmethod
    def print_intro():
        print('Welcome to Snoodle Test Runner \n'
              '-------------------------------------------')

    def find_test_files(self, path):
        if path == "__pycache__":
            return
        if os.path.isdir(path):
            for nested_path in os.listdir(path):
                self.find_test_files(path + "/" + nested_path)
        elif path.endswith(".py"):
            self.files.append(path)

    @staticmethod
    def find_test_classes(mod):
        return [c[1] for c in getmembers(mod) if isclass(c[1]) and c[0].startswith("Test")]

    @staticmethod
    def load_module(file, modnr):
        loader = importlib.machinery.SourceFileLoader(f"mod{modnr}", file)
        mod = types.ModuleType(loader.name)
        loader.exec_module(mod)
        return mod

    def run_file(self, file, modnr):
        print(f"Running file {file}")
        mod = self.load_module(file, modnr)
        classes = self.find_test_classes(mod)

        for test_class in classes:
            self.run_class_tests(test_class)

    def run_class_tests(self, test_class):
        obj = test_class()
        empty_function = lambda: None
        before_all = getattr(obj, "before_all", empty_function)
        after_all = getattr(obj, "after_all", empty_function)
        before_test = getattr(obj, "before", empty_function)
        after_test = getattr(obj, "after", empty_function)

        before_all()

        for test_name in dir(obj):
            test = getattr(obj, test_name)
            if test_name.startswith("test_") and callable(test):
                before_test()
                self.run_test((test_name, getattr(obj, test_name)))
                after_test()

        after_all()

    def run_test(self, test):
        (test_name, test_function) = test
        try:
            test_function()
            self.successes += 1
            print(f"{GREEN}{test_name} passed{RESET}")
        except FailedExpectation as e:
            print(f"{RED}{test_name} failed, {e.message}{RESET}")
            self.failures += 1
            self.failingFiles.append(test_name)

    def run(self):
        self.print_intro()
        for (i, file) in enumerate(self.files):
            self.run_file(file, i)
        self.print_summary()

    def print_summary(self):
        result = "Success" if self.failures == 0 else f"{self.failures} Failures"

        print("-------------------------------------------")
        print(f"Test run completed, result: {result}")
        print(f"Number of successes: {self.successes}")
        print(f"Number of failures: {self.failures}")
        print("-------------------------------------------")
        print("Files with Failing Tests: ")
        for failure in self.failingFiles:
            print(f"{RED}{failure}{RESET}")


def main():
    Runner(sys.argv[1]).run()


if __name__ == '__main__':
    main()

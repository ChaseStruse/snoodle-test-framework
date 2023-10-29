import importlib.machinery
import types
from inspect import getmembers, isclass
import os
from collections import defaultdict
from snoodle_test.colors import RED, GREEN, RESET
from snoodle_test.expectations import FailedExpectation
from snoodle_test.output import print_intro, print_summary


class Runner:
    def __init__(self, path):
        self.files = []
        self.successes, self.failures = 0, 0
        self.find_test_files(path)
        self.failing_methods = defaultdict(dict)
        self.successful_methods = defaultdict(dict)

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
            self.run_class_tests(test_class, file)

    def run_class_tests(self, test_class, file_name: str) -> None:
        obj = test_class()
        setup_tests = getattr(obj, "setup_tests", lambda: None)
        teardown_tests = getattr(obj, "teardown_tests", lambda: None)

        setup_tests()

        for test_name in dir(obj):
            test = getattr(obj, test_name)
            if test_name.startswith("test_") and callable(test):
                self.run_test(test_name=test_name, test_function=getattr(obj, test_name), file_name=file_name)

        teardown_tests()

    def add_success_message_to_dict(self, test_name: str, file_name: str) -> None:
        self.successes += 1
        success_message = f"{GREEN}{test_name}{RESET}"
        if self.successful_methods[file_name]:
            self.successful_methods[file_name][self.successes] = success_message
        else:
            self.successful_methods[file_name] = {self.successes: success_message}

    def add_failing_message_to_dict(self, test_name: str, file_name: str, error_message: str) -> None:
        self.failures += 1
        failing_message = f"{RED}Failing Method: {test_name} Reason for failure: {error_message}{RESET}"
        if self.failing_methods[file_name]:
            self.failing_methods[file_name][self.failures] = failing_message
        else:
            self.failing_methods[file_name] = {self.failures: failing_message}

    def run_test(self, test_name: str, test_function, file_name: str) -> None:
        try:
            test_function()
            self.add_success_message_to_dict(test_name, file_name=file_name)
            self.successes += 1

        except FailedExpectation as e:
            self.add_failing_message_to_dict(test_name=test_name, file_name=file_name, error_message=e.message)

    def run(self) -> None:
        print_intro()
        for (i, file) in enumerate(self.files):
            self.run_file(file, i)
        print_summary(failing=self.failing_methods, passing=self.successful_methods)

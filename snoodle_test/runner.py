import os
from collections import defaultdict
from snoodle_test.utils.colors import RED, GREEN, RESET
from snoodle_test.expectations import FailedExpectation
from snoodle_test.utils.console_output_utils import print_intro, print_summary
from snoodle_test.utils.runner_utils import load_module, find_test_classes


class Runner:
    def __init__(self, path):
        # Defaulting values
        self.files = []
        self.successes, self.failures = 0, 0
        self.failing_methods = defaultdict(dict)
        self.successful_methods = defaultdict(dict)
        # Initiating the run so users have better experience
        self.find_test_files(path)
        self.run()

    def find_test_files(self, path) -> None:
        """
        This loops through the given directory and attempts to find files with .py, it will continue to recursively call
        until it is completed.
        :param path: Path to test directory
        """

        if path == "__pycache__":
            return
        if os.path.isdir(path):
            for nested_path in os.listdir(path):
                self.find_test_files(path + "/" + nested_path)
        elif path.endswith(".py"):
            self.files.append(path)

    def run_file(self, file, modnr) -> None:
        """
        Finds all test classes and then loops through and runs them individually.
        :param file: Name of the file
        :param modnr: Module
        """
        print(f"Running file {file}")
        mod = load_module(file, modnr)
        classes = find_test_classes(mod)

        for test_class in classes:
            self.run_class_tests(test_class, file)

    def run_class_tests(self, test_class, file_name: str) -> None:
        """
        Runs the tests within the given test class
        :param test_class: Class object that holds the tests
        :param file_name: File name which is used for logging
        """
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
        """
        Adds the name of the test as the key and the message returned as the value. Also increases successes by 1.
        :param test_name: Name of the test
        :param file_name: Name of the file
        """
        self.successes += 1
        success_message = f"{GREEN}{test_name}{RESET}"
        if self.successful_methods[file_name]:
            self.successful_methods[file_name][self.successes] = success_message
        else:
            self.successful_methods[file_name] = {self.successes: success_message}

    def add_failing_message_to_dict(self, test_name: str, file_name: str, error_message: str) -> None:
        """
        Adds the name of the test as the key and the message returned as the value. Also increases failures by 1.
        :param test_name: Name of the test
        :param file_name: Name of the file
        :param error_message: Message that comes from the exception
        """
        self.failures += 1
        failing_message = f"{RED}Failing Method: {test_name} {RESET}|{RED} Reason: {error_message}{RESET}"
        if self.failing_methods[file_name]:
            self.failing_methods[file_name][self.failures] = failing_message
        else:
            self.failing_methods[file_name] = {self.failures: failing_message}

    def run_test(self, test_name: str, test_function, file_name: str) -> None:
        """
        Runs the given test function, either adds success or failure message depending.
        :param test_name: Name of the test
        :param test_function: Executable function
        :param file_name: Name of the file
        """
        try:
            test_function()
            self.add_success_message_to_dict(test_name, file_name=file_name)

        except FailedExpectation as e:
            self.add_failing_message_to_dict(test_name=test_name, file_name=file_name, error_message=e.message)

    def run(self) -> None:
        """
        Main access point. Ran at the end of the init.
        """
        print_intro()
        for (i, file) in enumerate(self.files):
            self.run_file(file, i)
        print_summary(failing=self.failing_methods, passing=self.successful_methods, total_failing=self.failures,
                      total_passing=self.successes)

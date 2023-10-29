from snoodle_test.colors import GREEN, RED, RESET


def print_intro():
    print('Welcome to Snoodle Test Runner \n'
          '-------------------------------------------')


def print_results(methods_list):
    for file_name in methods_list:
        print(file_name)

        for method_passing in methods_list[file_name].values():
            print(f"- {method_passing}")


def print_summary(failing, passing, total_failing, total_passing):
    print("-------------------------------------------")
    print(f"Test Run Completed")
    print("-------------------------------------------")
    print(f"Number of successes: {total_passing}")
    print("-------------------------------------------")
    print_results(methods_list=passing)
    print("-------------------------------------------")
    print(f"Number of failures: {total_failing}")
    print("-------------------------------------------")
    print_results(methods_list=failing)
    print("-------------------------------------------")
    print(f"Results: {GREEN}{total_failing} passed{RESET} | {RED}{total_failing} failed{RESET}")

# snoodle-test-framework

Test framework created using Python. This is just a fun project that I wanted to create just to see what I could to do.

## Running

- Pull the latest code from master 
- Navigate to the snoodle-test-framework directory
- Run the following command
    - python -m snoodle_test.runner example_tests
- This should then run the tests 3 should succeed and 3 should fail

### Setting up test files

- Test class must begin with Test, for example TestString, TestBoolean, etc
- Currently you can use isEqual and isNotEqual
- For some example tests checkout the example-tests folder
import pytest
# Write custom report functions for pytest 



def pytest_terminal_summary(terminalreporter, exitstatus, config):
    reports = terminalreporter.getreports('')
    for report in reports:
        # print status of each test
        print(report.outcome)
    # Report the number of tests that passed, failed, and skipped
    terminalreporter.write_sep("-", "test session summary")
    terminalreporter.write_line("passed: ")


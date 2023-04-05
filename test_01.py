from task_01 import is_even
def test_task_01():
    assert is_even(2) is True, "2 is even"
    assert is_even(3) is False, "3 is odd"
    assert is_even(8) is True, "8 is even"
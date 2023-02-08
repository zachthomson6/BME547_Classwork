import pytest

def test_add():
    from add import add
    answer = add(0.1, 0.2)
    assert answer == pytest.approx(0.3)

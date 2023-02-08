import pytest

@pytest.mark.parametrize("first_input, second_input, x_input, expected",
[((1,2),(2,3),3,4),
 ((-1,0),(0,-1),1,-2)
 ])

def test_yline(first_input,second_input,x_input, expected):
    from yline import yline
    answer = yline(first_input,second_input,x_input)
    assert answer == expected

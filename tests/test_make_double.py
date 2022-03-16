import pytest

@pytest.mark.parametrize("a, answer", [(6, 36), (7, 49), (8, 7)])
def test_make_double(a, answer):
    
    if a > 7:
        b = 7
    else:
       b = a * a
    
    assert b == answer


from src.pckg.features.create_double import compute_square
from unittest import mock

def test_compute_square():
    
    #with mock.patch('src.pckg.features.create_double.spc', return_value=2):
    with mock.patch('src.pckg.features.create_double.spc') as spc:
        spc.return_value = 1
        b = compute_square(4)
    
    assert b == 16
    
    return None
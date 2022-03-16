from src.pckg.features.create_double import make_double

def test_make_double():
    
    b = make_double(4)
    
    assert b == 8
    
    return None
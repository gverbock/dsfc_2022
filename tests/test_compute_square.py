import pandas as pd

def test_compute_square():
    
    df = pd.DataFrame({"A": [1, 2, 3], "B": [2, 3, 5]})
    
    assert df.shape == (3, 2)
    assert df.sum().sum() == 17

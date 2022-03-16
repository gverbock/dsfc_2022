from src.pckg.utils.transform import transform_string_int

class TestTransformStringToInt(object):
    
    def test_on_regular(self):
        """
        Perform a test on regular value
        """        
        a = transform_string_int("45")
        
        assert a == 45
        
        return None
    
    
    def test_on_comma(self):
        """
        Perform a test with a comma
        """
        
        a = transform_string_int("1,43")
        
        assert a == 143
        
        return None
    

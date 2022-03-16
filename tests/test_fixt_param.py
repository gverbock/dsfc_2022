import pytest
import re

@pytest.fixture(params = ['def12@34','34dger','12976456654434'])
def regex_input(request):
    return request.param

def test_regext(regex_input):
    assert re.findall(r".*(\d{2})", regex_input)[0] == "34"

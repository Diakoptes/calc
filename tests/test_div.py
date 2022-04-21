from calculator import Calculator
from layout import*
import pytest

def setup_module():
    print('\n===Setup Module===')

def test_div():
    assert Calculator.calc_div(10, 1) == 10



 
def teardown_module():
    print('\n===Teardown Module===')



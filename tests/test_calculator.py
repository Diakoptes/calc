from program.calculator import Calculator

def setup_module():
    print('\n===Setup Module===')

def test_sum():
    assert Calculator.calc_sum(5, 5) == 10

def test_sub():
    assert Calculator.calc_sub(10, 5) == 5

def test_multi():
    assert Calculator.calc_multi(10, 2) == 20

def test_div():
    assert Calculator.calc_div(10, 1) == 10

def test_exp():
    assert Calculator.calc_exp(10, 2) == 100

def test_mod():
    assert Calculator.calc_mod(10, 3) == 1

def teardown_module():
    print('\n===Teardown Module===')



from calculator import calc_mod

def test_calc_exp():
    
    first_num = float(10)
    second_num = float(4)
    
    mod = calc_mod(first_num, second_num)
   
    assert mod == 2

def test_calc_exp_negative():

    first_num = float(5)
    second_num = float(2)

    mod = calc_mod(first_num, second_num)

    assert mod != 2    
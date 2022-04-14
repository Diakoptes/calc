from calculator import calc_exp

def test_calc_exp():
    
    first_num = float(-2)
    second_num = float(4)
    
    exp = calc_exp(first_num, second_num)
   
    assert exp == 16

def test_calc_exp_negative():

    first_num = float(10)
    second_num = float(2)

    exp = calc_exp(first_num, second_num)

    assert exp != 200    
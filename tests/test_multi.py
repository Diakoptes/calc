from calculator import calc_multi

def test_calc_multi():
    
    first_num = float(2)
    second_num = float(11)
    
    multi = calc_multi(first_num, second_num)
   
    assert multi == 22

def test_calc_multi_negative():

    first_num = float(11)
    second_num = float(11)

    multi = calc_multi(first_num, second_num)

    assert multi != 100
from calculator import calc_sub

def test_calc_sub():
    
    first_num= float(20)
    second_num = float(11)
    
    sub = calc_sub(first_num, second_num)
   
    assert sub == 9

def test_calc_sub_negative():

    first_num = float(11)
    second_num = float(11)

    sub = calc_sub(first_num, second_num)

    assert sub != 100
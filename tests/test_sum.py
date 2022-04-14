from calculator import calc_sum

def test_calc_sum():
    
    first_num= float(1)
    second_num = float(11)
    
    sum = calc_sum(first_num, second_num)
   
    assert sum == 12

def test_calc_sum_negative():

    first_num= float(1)
    second_num = float(11)

    sum = calc_sum(first_num, second_num)

    assert sum != 100
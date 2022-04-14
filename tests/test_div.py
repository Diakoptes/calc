from calculator import calc_div

def test_calc_div():
    
    first_num = float(33)
    second_num = float(11)
    
    div = calc_div(first_num, second_num)
   
    assert div == 3

def test_calc_div_negative():

    first_num = float(100)
    second_num = float(1)

    div = calc_div(first_num, second_num)

    assert div != 200    
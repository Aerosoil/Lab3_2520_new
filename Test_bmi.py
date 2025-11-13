import Lab2_2520_new.bmi as bmi 

def test_CalcBMI_underweight():
    expected = -1
    result = bmi.calculate_bmi(1.75, 37)
    assert (result == expected)

def test_CalcBMI_normalweight():
    expected = 0
    result = bmi.calculate_bmi(1.75, 70)
    assert (result == expected)

def test_CalcBMI_overweight():
    expected = 1
    result = bmi.calculate_bmi(1.75, 100)
    assert (result == expected)
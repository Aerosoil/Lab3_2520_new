import employee_info as EMPINFO
from employee_info import employee_data as EMPDATA

def test_get_employees_by_age_range():
    expected = [EMPDATA[0], EMPDATA[3], EMPDATA[4]]
    answer = EMPINFO.get_employees_by_age_range(29, 36)
    assert (answer == expected)

def test_calculate_average_salary():
    expected = 60166.67
    result = EMPINFO.calculate_average_salary()
    assert (result == expected)

def test_get_employees_by_dept():
    expected = [EMPDATA[0], EMPDATA[5]]
    ## expected = [EMPDATA[0], EMPDATA[-1]]
    result = EMPINFO.get_employees_by_dept('Sales')
    assert (result == expected)
import pytest

def test_hdl_analysis_1():
    from blood_calculator import hdl_analysis
    answer = hdl_analysis(65)
    expected = "Normal"
    assert answer == expected

def test_hdl_analysis_2():
    from blood_calculator import hdl_analysis
    answer = hdl_analysis(45)
    expected = "Borderline Low"
    assert answer == expected

def test_hdl_analysis_3():
    from blood_calculator import hdl_analysis
    answer = hdl_analysis(1)
    expected = "Low"
    assert answer == expected

@pytest.mark.parametrize("HDL_value, expected",[
    (65, "Normal"), (45, "Borderline Low"),
    (15, "Low")])
def test_hdl_analysis(HDL_value, expected):
    from blood_calculator import hdl_analysis
    answer = hdl_analysis(HDL_value)
    assert answer == expected

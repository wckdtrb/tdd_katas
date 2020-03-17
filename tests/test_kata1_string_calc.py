from katas import kata1_string_calc
import pytest

def test_str_add_empty():
    assert kata1_string_calc.str_add("") == 0

def test_str_add_one():
    assert kata1_string_calc.str_add("1") == 1

def test_str_add_one_and_empty():
    assert kata1_string_calc.str_add("1,") == 1

def test_str_add_one_and_one():
    assert kata1_string_calc.str_add("1, 1") == 2

def test_str_add_arranged():
    arranged = str([x for x in range(5)]).strip('[]')
    assert kata1_string_calc.str_add(arranged) == 10

def test_str_add_newlines():
    assert kata1_string_calc.str_add('1\n2,3') == 6

def test_str_add_different_delimiters():
    assert kata1_string_calc.str_add('//;\n1;2') == 3

def test_str_add_negative():
    with pytest.raises(AssertionError):
        kata1_string_calc.str_add('-1')
    
def test_str_add_negative_list():
    with pytest.raises(AssertionError) as execinfo :
        kata1_string_calc.str_add('-1, -2')
    assert "'-1', '-2'" in str(execinfo.value)

def test_str_add_over_one_thousand():
    assert kata1_string_calc.str_add('1001, 1') == 1

def test_str_add_long_delimiters():
    assert kata1_string_calc.str_add("//[***]\n1***2***3") == 6

def test_str_add_multi_delimeters():
    assert kata1_string_calc.str_add("//[*][%]\n1*2%3") == 6
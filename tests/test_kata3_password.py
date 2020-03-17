from katas import kata3_password as password
import pytest

def test_verify():
    assert password.verify('Abracadabra1') == 'Abracadabra1'

def test_verify_too_short():
    with pytest.raises(AssertionError) as execinfo:
        password.verify('012345a')
    
    assert "Password must be more than 8 characters" in str(execinfo)

def test_verify_null():
    with pytest.raises(AssertionError) as execinfo:
        password.verify('')
    
    assert "Password must contain at least 1 lowercase letter" in str(execinfo)

def test_verify_one_upper():
    with pytest.raises(AssertionError) as execinfo:
        password.verify('abcdegh')
    
    assert "Password must contain at least 1 uppercase letter" in str(execinfo)

def test_verify_one_lower():
    with pytest.raises(AssertionError) as execinfo:
        password.verify('ABCDFGH')
    
    assert "Password must contain at least 1 lowercase letter" in str(execinfo)

    with pytest.raises(AssertionError) as execinfo:
        password.verify('ABC123DEF')
    
    assert "Password must contain at least 1 lowercase letter" in str(execinfo)


def test_verify_one_number():
    with pytest.raises(AssertionError) as execinfo:
        password.verify('ABCeFG')
    
    assert "Password must contain at least 1 number" in str(execinfo)

def test_verify_three_of_four():
    assert password.verify('abracad1') == 'abracad1'
    assert password.verify('Abra1') == 'Abra1'
    assert password.verify('AbraCaDabra') == 'AbraCaDabra'
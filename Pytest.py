import pytest
def is_negative_number(number):
    if number < 0:
        return True
    else:
        return False

def test_negative_number():
    assert is_negative_number(-5) == True
    assert is_negative_number(0) == False
    assert is_negative_number(10) == False
    assert is_negative_number(-10) == True

def test_input_number():
    pass

if __name__ == "__main__":
    pytest.main()
############################################################################################
def is_even(number):
    return number % 2 == 0

def test_even_number():
    assert is_even(4) == True

def test_odd_number():
    assert is_even(7) == False

def test_zero():
    assert is_even(0) == True

if __name__ == '__main__':
    pytest.main()
############################################################################################
def count_digits(number):
    return len(str(number))

def test_count_digits_zero():
    assert count_digits(0) == 1

def test_count_digits_positive():
    assert count_digits(12345) == 5

def test_count_digits_negative():
    assert count_digits(-9876) == 5

def test_count_digits_large_number():
    assert count_digits(123456789012345678901234567890) == 30

if __name__ == "__main__":
    pytest.main()
############################################################################################
def sum_of_list_elements(lst):
    return sum(lst)

def test_sum_of_list_elements():
    input_list = [1, 2, 3, 4, 5]
    expected_result = 15
    result = sum_of_list_elements(input_list)
    
    assert result == expected_result

if __name__ == '__main__':
    pytest.main()
############################################################################################
def sum_numbers(numbers_str):
    numbers = [int(num) for num in numbers_str.split(',')]
    return sum(numbers)

def test_sum_numbers():
    assert sum_numbers('12,34,56') == 102

if __name__ == '__main__':
    pytest.main()
############################################################################################



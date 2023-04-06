import pytest
from series.series import Fibonacci
from series.series import Lucas
from series.series import sum_series

#______________________________________________Fibonacci__________________________________________________

"""
    Computes the nth Fibonacci number.

    Parameters:
    n (int): The index of the Fibonacci number to compute.

    Returns:
    int: The nth Fibonacci number.

    Examples:
    >>> Fibonacci(0)
    0
    >>> Fibonacci(1)
    1
    >>> Fibonacci(10)
    55

"""


def test_Fibonacci_one():
    actual = Fibonacci(0)
    expected = 0
    assert actual == expected # assert : is actual equal the expected

def test_Fibonacci_two():
    actual = Fibonacci(1)
    expected = 1
    assert actual == expected # assert : is actual equal the expected

def test_Fibonacci_three():
    actual = Fibonacci(2)
    expected = 1 
    assert actual == expected # assert : is actual equal the expected

def test_Fibonacci_four():
    actual = Fibonacci(3)
    expected = 2
    assert actual == expected # assert : is actual equal the expected

def test_Fibonacci_five():
    actual = Fibonacci(4)
    expected = 3
    assert actual == expected # assert : is actual equal the expected

def test_Fibonacci_six():
    actual = Fibonacci(5)
    expected = 5
    assert actual == expected # assert : is actual equal the expected

def test_Fibonacci_seven():
    actual = Fibonacci(6)
    expected = 8
    assert actual == expected # assert : is actual equal the expected

def test_Fibonacci_eight():
    actual = Fibonacci(7)
    expected = 13
    assert actual == expected # assert : is actual equal the expected


#______________________________________________Lucas__________________________________________________


"""
    Computes the nth Lucas number.

    Parameters:
    n (int): The index of the Lucas number to compute.

    Returns:
    int: The nth Lucas number.

    Examples:
    >>> Lucas(0)
    2
    >>> Lucas(1)
    1
    >>> Lucas(10)
    123

"""


def test_Lucas_one():
    actual = Lucas(0)
    expected = 2
    assert actual == expected # assert : is actual equal the expected

def test_Lucas_two():
    actual = Lucas(1)
    expected = 1
    assert actual == expected # assert : is actual equal the expected

def test_Lucas_three():
    actual = Lucas(2)
    expected = 3
    assert actual == expected # assert : is actual equal the expected

def test_Lucas_four():
    actual = Lucas(3)
    expected = 4
    assert actual == expected # assert : is actual equal the expected

def test_Lucas_five():
    actual = Lucas(4)
    expected = 7
    assert actual == expected # assert : is actual equal the expected

def test_Lucas_six():
    actual = Lucas(5)
    expected = 11
    assert actual == expected # assert : is actual equal the expected

def test_Lucas_seven():
    actual = Lucas(6)
    expected = 18
    assert actual == expected # assert : is actual equal the expected

def test_Lucas_eight():
    actual = Lucas(7)
    expected = 29
    assert actual == expected # assert : is actual equal the expected


#______________________________________________sum_series__________________________________________________


"""
    Computes the nth number in a series defined by the values of a and b.

    If a=0 and b=1, the series is the Fibonacci sequence.
    If a=2 and b=1, the series is the Lucas sequence.
    If a and b are any other values, the series is defined by the recurrence relation: sum_series(n-1,a,b) + sum_series(n-2,a,b)

    Parameters:
    n (int): The index of the number to compute in the series.
    a (int, optional): The first value in the series. Default is 0.
    b (int, optional): The second value in the series. Default is 1.

    Returns:
    int: The nth number in the series.

"""

def test_sum_series():
    actual=sum_series(2,3,4)
    expected=7
    assert actual == expected
def test_sum_series_1():
    actual=sum_series(5,1,4)
    expected=23
    assert actual == expected
def test_sum_series_2():
    actual=sum_series(5)
    expected=5
    assert actual == expected
def test_sum_series_2():
    actual=sum_series(5,2,1)
    expected=11
    assert actual == expected

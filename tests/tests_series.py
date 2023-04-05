import pytest
from series.series import Fibonacci
from series.series import Lucas

#______________________________________________Fibonacci__________________________________________________


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


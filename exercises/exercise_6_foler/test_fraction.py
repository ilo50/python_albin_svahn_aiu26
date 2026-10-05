from pytest import raises
from fraction import Fraction

'''
The tests are:
1/2 + 1/3 = 5/6
1/2 - 1/3 = 1/6
7/6 --> 1 1/6 (mixed)
3*1/2 = 3/2
1/2 * 3 = 3/2
1/4 + 2 = 9/4
1/4 / 1/2 = 1/2
2/4 == 1/2 --> True
3/4 += 2 = 11/4

'''

def test_valid_addition():

    f1 = Fraction(1, 2)
    f2 = Fraction(1, 3)
    assert f1.addition(f2) == Fraction(5, 6)

def test_invalid_addition():

    with raises(TypeError):
        Fraction("4", 5)

    with raises(ValueError):
        Fraction()


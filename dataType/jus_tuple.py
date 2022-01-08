import pytest


def test_tuples_basic():
    t1 = (1,2,3)
    assert isinstance(t1, tuple)
    assert t1[0] == 1

    t2 = tuple((1,2,3))
    assert isinstance(t2, tuple)
    assert t2[0] == 1

    fruits = ('apple', 'banana', 'orange', 'mango')
    assert len(fruits)== 4
    assert fruits[1:] == ('banana', 'orange', 'mango')
    
    fruits2 = ('waftermelon', 'kiwi')
    assert fruits2 * 3 ==  ('waftermelon', 'kiwi', 'waftermelon', 'kiwi', 'waftermelon', 'kiwi')
    assert fruits + fruits2 == ('apple', 'banana', 'orange', 'mango', 'waftermelon', 'kiwi')

    fruits3 = fruits, ('peach')
    assert fruits3 == (('apple', 'banana', 'orange', 'mango'), ('peach'))


if __name__ == "__main__":
    test_tuples_basic()


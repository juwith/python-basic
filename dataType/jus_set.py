import pytest

# set의 특징
#  - 순서가 없다.
#  - 중복이 없다. 

def test_set():
    stock_set = {"samsung","hyundai","hynix"}
    assert isinstance(stock_set, set)

    set0 = {1,2,1,1,1,1,3}
    assert set0 == {1,2,3} # 순서가 없으며 중복이 없다.
    assert set0 == {3,1,2} # 순서가 없으며 중복이 없다.
    
    set0.add(4)
    assert set0 == {1,2,3,4}

    set0.update([5,6,7])
    assert set0 == {1,2,3,4,5,6,7}

    set0.remove(5)
    assert set0 == {1,2,3,4,6,7}

    set1 = {'a','b','c','d'}
    set2 = {'d','e','f'}

    assert set1 & set2 == {'d'} # 교집합
    assert set1 | set2 == {'a','b','c','d','e','f'}
    assert set1 - set2 == {'a','b','c'}
    assert set2 - set1 == {'e','f'}

    assert set1 ^ set2 == {'a','b','c','e','f'} # 중복되지 않는 원소(xor)


if __name__ == "__main__":
    test_set()

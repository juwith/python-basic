import pytest
# $ pytest jus_list.py

# 기본 배열 순서 [0], [1], ...[n]
# 역순 [-1]
# 범위 [2:4] : [2], [3] 하지만 [4]는 포함되지 않는다.
#      [:2] : [0], [1]
#      [2:] : [2], [3], ..., [n]
# 연산 : +(append), *(반복)
def test_list_basic():
    # 숫자형
    num_list = [1, 2, 3, 4, 5]
    assert num_list[0] == 1

    num_list2 = [37, 27, 55, 14, 95]
    assert num_list2[3] + num_list2[4] == 109 # 14 + 95
    assert num_list2[2:4] == [55, 14] # [2],[3]
    assert num_list2[:2] == [37, 27] # [0], [1]
    assert num_list2[2:] == [55, 14, 95] # [2], [3], [4]
    assert num_list2[:] == [37, 27, 55, 14, 95] # [0] ~ [4]

    # 문자형
    str_list = ['my', 'name', 'is', 'jusang']
    assert str_list[0] == 'my'
    assert len(str_list) == 4 # 크기
    str_list[:] = [] # clear list
    assert str_list == []

    # 2차원 list
    cmpx_list = [1, 2, ['my', 'name']]
    assert cmpx_list == [1, 2, ['my', 'name']]
    assert cmpx_list[0] == 1
    assert cmpx_list[2] == ['my', 'name']
    assert cmpx_list[2][0] == 'my'

    # 빈 list 선언
    empty_list = list()

    # 연산
    num_list3 = [1, 2, 3, 4, 5]
    num_list3 += [6] # list 6을 끝에 넣음
    num_list3.append(7) # 7을 리스트 끝에 넣음
    assert num_list3 == [1, 2, 3, 4, 5, 6, 7]
    num_list3 *= 2
    assert num_list3 == [1, 2, 3, 4, 5, 6, 7, 1, 2, 3, 4, 5, 6, 7]

def test_list_method():
    companies = ['Samsung', 'Hynix']
    companies.append('Hyundai') # 또는 ['ABC', 'DEF']와 같이 list로 append 가능
    assert companies == ['Samsung', 'Hynix', 'Hyundai']

    companies.remove('Hynix')
    assert companies == ['Samsung', 'Hyundai']

    companies.insert(0,'Kakao')
    companies.append('Samsung')
    assert companies == ['Kakao', 'Samsung', 'Hyundai', 'Samsung']

    assert companies.index('Samsung') == 1 # 해당 factor가 있는 index를 반환
    assert companies.index('Samsung', 2) == 3 # 2번 factor부터 시작, 해당 factor가 있는 index를 반환
    assert companies.count('Samsung') == 2 # 해당 factor의 개수를 반환

    companies.reverse() # reverse
    assert companies == ['Samsung', 'Hyundai', 'Samsung', 'Kakao']

    companies.sort() # 정렬, 문자의 경우 알파벳 순으로 정렬
    assert companies == ['Hyundai', 'Kakao', 'Samsung', 'Samsung']

    my_factor = companies.pop() # 가장 뒤의 factor를 끄집어냄
    assert my_factor == 'Samsung'

    my_factor = companies.pop(0) # 해당 index의 factor를 끄집어냄
    assert my_factor == 'Hyundai'

def test_list_advanced():
    evens = [x *2 for x in range(10)]
    assert evens == [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

    # list를 이용한 for문 2중 중첩 예제
    animals = ['cat', 'dog', 'monkey']
    fruits = ['apple', 'banana', 'cherry']

    combinations = []
    for first in animals:
        for second in fruits:
            combinations.append((first, second))
    assert combinations == [('cat', 'apple'), ('cat', 'banana'), ('cat', 'cherry'), 
                            ('dog', 'apple'), ('dog', 'banana'), ('dog', 'cherry'), 
                            ('monkey', 'apple'), ('monkey', 'banana'), ('monkey', 'cherry')]

    combinations = [(x, y) for x in animals for y in fruits] # 위의 2중 for문과 동일함.
    assert combinations == [('cat', 'apple'), ('cat', 'banana'), ('cat', 'cherry'), 
                            ('dog', 'apple'), ('dog', 'banana'), ('dog', 'cherry'), 
                            ('monkey', 'apple'), ('monkey', 'banana'), ('monkey', 'cherry')]

    # 예제2
    numbers = [-3, -2, -1, 0, 1, 2, 3]
    numbers_plus_1 = [x +1 for x in numbers]
    assert numbers_plus_1 == [-2, -1, 0, 1, 2, 3, 4]

    number_unsigned = [x for x in numbers if x >= 0]
    assert number_unsigned == [0, 1, 2, 3]

    # 예제3, tuple 만들기
    number_tuple = [(x, x+1) for x in numbers]
    assert number_tuple == [(-3,-2), (-2,-1), (-1,0), (0,1), (1,2), (2,3), (3,4)]

    # 예제4 1차원 list로 만들기
    numbers2x2 = [[0,1], [2,3]]
    numbers_1 = []
    for elem in numbers2x2:
        for num in elem:
            numbers_1.append(num)
    assert numbers_1 == [0, 1, 2, 3]
    
    numbers_1 = [num for elem in numbers2x2 for num in elem] # 위의 2중 for문과 동일함
    assert numbers_1 == [0, 1, 2, 3]



if __name__ == "__main__":
    test_list_basic()
    test_list_method()
    test_list_advanced()
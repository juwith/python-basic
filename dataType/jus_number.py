# isinstance(object, classinfo) : 자료형을 확인하는 함수
# assert : 조건이 참이 아니면 프로그램 중단(디버그 모드에서만)
#        예) assert True : 이상 없음
#            assert False : 프로그램 중단, 오류 발생

# int type
int_pos = 1000
int_neg = -1000
assert isinstance(int_pos, int) # 만약 int_pos가 int형이면 True를 반환
assert isinstance(int_neg, int)

# bool type
bool_true = True
bool_false = False
assert isinstance(bool_true, bool)
assert isinstance(bool_false, bool)

# float type
float_pos = 100.0
float_neg = -100.0
float_trans = float(50)
assert isinstance(float_pos, float)
assert isinstance(float_neg, float)
assert isinstance(float_trans, float)

# complex type
complex_num1 = 1 + 1j
complex_num2 = 1 - 1j
assert isinstance(complex_num1, complex)
assert isinstance(complex_num2, complex)

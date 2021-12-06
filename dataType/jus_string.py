# isinstance(object, classinfo) : 자료형을 확인하는 함수

#####################
# 1. String type
#####################
str_1 = "My name is Jusang" # double quotes.
str_2 = 'My name is Jusang' # single quotes.
# print("str_1 :" + str_1)
# print("str_2 :" + str_2)
assert str_1 == str_2

multi_line_str_1 = """\
My 
name 
is 
Jusang
"""

multi_line_str_2 = '''\
My 
name 
is 
Jusang
'''
assert multi_line_str_1 == multi_line_str_2
# print("multi_line_str_1 :" + multi_line_str_1)
# print("multi_line_str_2 :" + multi_line_str_2)

str_complex = "\\My name is\\ \n \'jusang\'"
print("str_complex : " + str_complex)

str_word = "My name is Jusnag" #[0]='M', [1]='y', [2]=' ', [3]='n' ...
# [n:m] => 배열의n 번째 인덱스 부터 인덱스m 까지 배열을 잘라냄
assert str_word[:2] == "My"
assert str_word[2:] == " name is Jusnag"
assert str_word[-2:] == "ag"
# print(str_word[:2]) # 배열의 0번째 부터 2번째(포함안함)까지
# print(str_word[2:]) # 배열의 2번째 부터 끝까지
# print(str_word[-2:]) # 배열의 끝부터 역순으로(-) 2번째 부터 끝까지

######################
# 2. String operating
######################

str_oper = 3 * 'my' + ' name'
assert str_oper == "mymymy name"
#print(str_oper)
str_oper_2 = 'My' ' name'
assert str_oper_2 == 'My name'
str_oper_3 = (
    'My name is '
    'Jusang'
)
assert str_oper_3 == 'My name is Jusang'

######################
# 3. String formatting
# %s:문자열, %c:문자 1개, %d:정수 %f:부동소수 %x:16진수
# 자리 수 표현
#  %.4f 소수점 4자리까지 표현
#  %5s 문자 5자리 표현(오른쪽 정렬)
#  %-5s 문자 5자리 표현(왼쪽 정렬)
######################
str_format = "my name is %s, I'm %d years old." % ('Jusang', 30)
assert str_format == "my name is Jusang, I'm 30 years old."

######################
# 4. String function
#######################

str_function = "0000my0name0is0Jusang0000"
assert str_function.strip('0') == 'my0name0is0Jusang' # 왼쪽과 오른쪽에서 해당 문자 제거
assert str_function.rstrip('0') == '0000my0name0is0Jusang' # 오른쪽에서 해당 문자 제거
assert str_function.lstrip('0') == 'my0name0is0Jusang0000' # 왼쪽에서 해당 문자 제거
str_function = "    my name is Jusang    "
assert str_function.strip() == "my name is Jusang" # 공백 입력 시 space 제거

str_function = "word"
assert len(str_function) == 4 # 문자열 크기

str_function = "WoRd"
assert str_function.lower() == 'word'
assert str_function.upper() == 'WORD'

str_function = "my name is Kelvin"
assert str_function.replace('Kelvin', 'Jusang') == 'my name is Jusang' # 문자열 교체

str_function = "my,name,is,Jusang"
assert str_function.split(',') == ['my', 'name', 'is', 'Jusang']

str_function = "a bb ccc dddd eeeee"
assert str_function.count('d') == 4 # 갯수 세기
assert str_function.count('dd') == 2 # 갯수 세기

assert str_function.find('d') == 9 # 문자열 위치, 만약 여러개면 첫 번째 위치, 없으면 -1
assert str_function.find('g') == -1

assert str_function.index('a') == 0 # find와 동작은 같으나, 없으면 error 발생

assert 'my name is jusang'.title() == 'My Name Is Jusang' # 첫 문자를 모두 대문자로

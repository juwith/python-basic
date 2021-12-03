# isinstance(object, classinfo) : 자료형을 확인하는 함수

# 1. String type
str_1 = "My name is Jusang" # double quotes.
print("str_1 :" + str_1)

str_2 = 'My name is Jusang' # single quotes.
print("str_2 :" + str_2)

multi_line_str_1 = """\
My 
name 
is 
Jusang
"""
print("multi_line_str_1 :" + multi_line_str_1)

multi_line_str_2 = '''\
My 
name 
is 
Jusang
'''
print("multi_line_str_2 :" + multi_line_str_2)

str_complex = "\\My name is\\ \n \'jusang\'"
print(str_complex)

str_word = "My name is Jusnag" #[0]='M', [1]='y', [2]=' ', [3]='n' ...
# [n:m] => 배열의n 번째 인덱스 부터 인덱스m 까지 배열을 잘라냄
print(str_word[:2]) # 배열의 0번째 부터 2번째(포함안함)까지
print(str_word[2:]) # 배열의 2번째 부터 끝까지
print(str_word[-2:]) # 배열의 끝부터 역순으로(-) 2번째 부터 끝까지

# 2. String type


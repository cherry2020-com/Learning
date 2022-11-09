# -*- coding: utf-8 -*-

L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]

# 打印Apple:
print(L[0][0])
# 打印Python:
print(L[1][1])
# 打印Lisa:
print(L[-1][-1])

# 切片 and 递归， 去除字符串前后的空格
str1 = '  dfjk  err   '
print(str1.split())
print(str1.strip())
print(len(str1))

def trim(s):
    i = 0
    j = len(s)
    while i<len(s) :
        i = i+1
        if s[i] != ' ':
            new_str = s[i:]
            break
    while j>0:
        j = j - 1
        if s[j] != ' ':
            new_str = new_str[:j-1]
            return new_str

def trim1(s):
    while s[0] == ' ':
        s = s[1:]
        trim1(s)
    while s[-1] == ' ':
        s = s[:-1]
        trim1(s)
    return s


print(trim1(str1))

# 列表生成式
test1 = [x for x in range(1, 11) if x % 2 == 0]
test2 = [x if x % 2 == 0 else -x for x in range(1, 11)]
print(test1)
print(test2)

L1 = ['Hello', 'World', 18, 'Apple', None]

L2 = [s.lower() for s in L1 if isinstance(s,str)]
print(L2)


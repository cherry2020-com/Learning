#!/usr/bin/python
# -*- coding: UTF-8 -*-
import math

###################
# 函数的调用
def quadratic(a, b, c):
    if a != 0:
        x = ((-b + math.sqrt(b * b - 4 * a * c))/(2*a),(-b - math.sqrt(b * b - 4 * a * c))/(2*a))
        return x
    elif (a == 0 and b != 0):
        x = -c / b
        return x
    else:
        raise Error('bad operand type')

# # 测试:
print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')


###################
# Python的函数具有非常灵活的参数形态，既可以实现简单的调用，又可以传入非常复杂的参数。
# 默认参数一定要用不可变对象，如果是可变对象，程序运行时会有逻辑错误！
# 要注意定义可变参数和关键字参数的语法：
# *args是可变参数，args接收的是一个tuple；
# **kw是关键字参数，kw接收的是一个dict。
# 以及调用函数时如何传入可变参数和关键字参数的语法：
# 可变参数既可以直接传入：func(1, 2, 3)，又可以先组装list或tuple，再通过*args传入：func(*(1, 2, 3))；
# 关键字参数既可以直接传入：func(a=1, b=2)，又可以先组装dict，再通过**kw传入：func(**{'a': 1, 'b': 2})。
# 使用*args和**kw是Python的习惯写法，当然也可以用其他参数名，但最好使用习惯用法。
# 命名的关键字参数是为了限制调用者可以传入的参数名，同时可以提供默认值。
# 定义命名的关键字参数在没有可变参数的情况下不要忘了写分隔符*，否则定义的将是位置参数。

########### 函数的默认参数
# 如果可以设计一个不变对象，那就尽量设计成不变对象。
# 设计str、None这样的不变对象呢？因为不变对象一旦创建，对象内部的数据就不能修改，这样就减少了由于修改数据导致的错误。
# 此外，由于对象不变，多任务环境下同时读取对象不需要加锁，同时读一点问题都没有。我们在编写程序时，

def add_end(L=[]):
    L.append('END')
    return L

print(add_end([1, 2, 3]))
print(add_end())
print(add_end())

def add_end_1(L=None):
    if L is None:
        L = []
    L.append('END')
    return L

print(add_end_1([1, 2, 3]))
print(add_end_1())
print(add_end_1())

# 有多个默认参数时，调用的时候，既可以按顺序提供默认参数，比如调用enroll('Bob', 'M', 7)，
# 意思是，除了name，gender这两个参数外，最后1个参数应用在参数age上，city参数由于没有提供，仍然使用默认值。
#
# 也可以不按顺序提供部分默认参数。当不按顺序提供部分默认参数时，需要把参数名写上。
# 比如调用enroll('Adam', 'M', city='Tianjin')，意思是，city参数用传进去的值，其他默认参数继续使用默认值。

def enroll(name, gender, age=6, city='Beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)

print(enroll('Bob', 'M', 7))
print(enroll('Adam', 'M', city='Tianjin'))
print(enroll('Adam', 'M', city='Tianjin', age=9))

########### 函数的可变参数
# 在参数前面加了一个*号
# 可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。
# 而关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict。

def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

print(calc(1,2,3,4,3))
a = [1,2,3,4,3]
print(calc(*a))
b = (1,2,3,4,3)
print(calc(*b))

########### 函数的关键字参数
# 可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。 *parameter
# 而关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict。 **parameter
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)

def person_1(name, age, *kw):
    print('name:', name, 'age:', age, 'other:', kw)

print(person('Michael', 30))
print(person_1('Michael', 30))
print(person('Adam', 45, gender='M', job='Engineer'))

# **extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数，
# kw将获得一个dict，注意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra。
extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, **extra)

########### 函数的命名关键字参数
# ,*, 如果要限制关键字参数的名字，就可以用命名关键字参数
# 命名关键字参数可以有缺省值，从而简化调用

def person(name, age, *, city, job):
    print(name, age, city, job)

print(person('Jack', 24, city='Beijing', job='Engineer'))

# 在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。
# 但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。

def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)

f1(1, 2)
f1(1,2,3)
f1(1, 2, 3, 'a', 'b')
f1(1, 2, 3, 'a', 'b', x=99)
f2(1, 2, d=99, ext=None)

args = (1, 2, 3, 4)
kw = {'d': 99, 'x': '#'}
f1(*args, **kw)

args = (1, 2, 3)
kw = {'d': 88, 'x': '#'}
f2(*args, **kw)

def product(x, *y):
    if y is not None:
        sum = x
        for i in y:
            sum = i * sum
        return sum

# type error
try:
    product()
    print('测试失败!')
except TypeError:
    print('测试成功!')
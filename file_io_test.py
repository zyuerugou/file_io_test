# -*- coding: utf-8 -*-
"""
从txt中读取行的测试
可以证明，文件对象作为参数传入函数，在函数内部进行读取内容之后，退出函数，光标位置保留

从txt中写入行的测试
可以证明，文件对象作为参数传入函数，在函数内部进行写入内容之后，退出函数，光标位置保留

@author: 193334
"""

filename = r'test.txt'

'''
# 读取
def b(f):
    str = f.readline()
    print('b:1')
    print(str)


def a(f):
    str = f.readline()
    print('a:1')
    print(str)
    
    b(f)
    
    str = f.readline()
    print('a:2')
    print(str)
    
    return str
'''

# 写入
def b(f):
    f.writelines('b:1\n')


def a(f):
    f.writelines('a:1\n')
    
    b(f)
    
    f.writelines('a:2\n')


if __name__ == '__main__':
    f = open(filename, 'w')
    
    a(f)
    
    f.close()
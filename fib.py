# -*- coding: utf-8 -*-
"""
Spyderエディタ

これは一時的なスクリプトファイルです
"""

def fib(n):
    a = 0
    b = 1
    for i in range(n):
        a, b = b, a + b
    return b

print(fib(2018))


    
    
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__' :

n = int(input("Value of n? "))
k = n // 7
r = n % 7
if r != 0:
    a = 7*k + r
    print("(n=7*k + r)","Ответ:", a)
elif r == 0:
    b = 7*k
    print("(n=7*k)","Ответ:", b)

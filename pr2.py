# -*- coding: utf-8 -*-
"""
Created on Sat May  1 15:32:40 2021

@author: USER
"""


def ch_prime(n):
    if n == 2:
        return True
    if n == 3:
        return True
    if n & 1 == 0:
        return False
    d= 3
    while d * d <= n:
        if n % d == 0:
            return False
        d= d + 2
    return True
def main():
    number = int(input())
    for _ in range(number):
        l_l,h_l = map(int,input().split(' '))
        h_l = h_l + 1
        val = list()
        if l_l == h_l:
            if ch_prime(h_l):
                print(0)
            else:
                print(-1)
        else:
            
            for i in range(l_l,h_l):
                if ch_prime(i):
                    val.append(i)
            print(val)
            if len(val) == 0:
                print(-1)
            elif len(val) == 1:
                print(0)
            else:
                print(val[-1]-val[0])
            
                
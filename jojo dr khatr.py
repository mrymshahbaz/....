# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 09:14:46 2024

@author: persian rayaneh
"""
def is_prime(num):
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return -1
    return 1


def check(x, y):
    for i in range(2, y):
        if x % i == 0:
            return True
    return False

n = int(input("enter number n:"))
m = int(input("enter number m:"))
k = 0
num = 0
prime_numbers = 0
for i in range(2, 5 + 1):
    if is_prime(i) == 1 and i ** 2 < n + 1:
        for j in range(i*2, n + 1, i):
            if not check(j, i):
                k += 1
                num = j
if k == num:
    print("You need to pay {} Billion!".format(num))
else:
    print(-2)

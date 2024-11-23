# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
n = int(input("enter n:"))
m = int(input("enter m:"))
cities = []
airlines = {}
for i in range(n):
    city = input("enter the city:")
    if not city in airlines.keys():
        airlines.update({city: []})
for i in range(m):
    flight = input("enter the origin & destination :")
    info = flight.split(" ")
    origin = info[0]
    destination = info[1]
    airlines[origin.title()].append(destination)
for i in airlines:
    l = len(airlines.get(i))
    print(l)
    if l:
        for j in airlines.get(i):
            print(j)

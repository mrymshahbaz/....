# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
n = int(input("enter the number of exams"))
grade_point = {"A":5, "B":4, "C":3, "D":2, "E":1}
all_units = 0
total_weight= 0
for i in range(n):
    x = str(input("enter the weight & score:\n"))
    score = int(x.split(" ")[0]) * grade_point[x.split(" ")[1].upper()]
    all_units += int(x.split(" ")[0])
    total_weight += score
print(all_units)
avg = total_weight//all_units +1
avg_in_letter = ""
print(grade_point.items())
for i in grade_point:
    if grade_point[i] == avg:
        avg_in_letter = i
        break
print("The average is: {}".format(avg_in_letter))

# -*- coding: UTF-8 -*-

# Filename : 01-string.py23
# author by : Steven Lu

# 目的:
# 玩转三角形


print('\n----玩转三角形 ----')
a = float(input('输入三角形第一边长 a =:  '))
b = float(input('输入三角形第一边长 b =:  '))
c = float(input('输入三角形第一边长 c =:  '))

if ( a + b > c) and (a + c > b ) and ( b + c > a ):
    if (abs(a - b) >= c) or (abs(a - c) >= b) or (abs(b - c) >= a):
        print("错误！某两边之差小于第三边，所以无法构成三角形。")
    else:
        if(a==b)or(b==c)or(a==c):
            print ('正确！可以组成等边或等腰三角形')
            print ('正确！可以组成不等边等边三角形')
else:
    print("错误！某两边之和小于第三边，所以无法构成三角形。")

# -*- coding: utf-8 -*-
"""Untitled8.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1IFSK8AMg4n9hNq7gHRGpEpH8Aqp0rEZD

SSTF
"""

queue = list(map(int, input('Enter sequence : ').split()))
header = int(input('Give header : '))
queue.insert(0, header)
path = [header]
cnt = len(queue) - 1
val = 0
print("Total Distance:")
while queue:

    if cnt == 0:
        queue.remove(header)
        hdr = path[len(path) - 1]
        minDist = 9999999999999999999
        for i in queue:
            if minDist > abs(hdr - i):
                minDist = abs(hdr - i)
                temp = i
        print('({}-{})'.format(hdr, temp))       
        path.append(temp)
        header = temp
    else:
        queue.remove(header)
        hdr = path[len(path) - 1]
        minDist = 9999999999999999999
        for i in queue:
            if minDist > abs(hdr - i):
                minDist = abs(hdr - i)
                temp = i
        print('({}-{})'.format(hdr, temp), end='+')
        val += abs(hdr - temp)
        path.append(temp)
        header = temp

    cnt -= 1
print("\n")
print('Path :', path[:-1])
print("\n")
print('Illustration shows total head movement of', val,'cylinders')
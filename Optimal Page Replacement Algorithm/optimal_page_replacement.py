# -*- coding: utf-8 -*-
"""Optimal_Page_Replacement.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1oe-TYEnDcbkegITfx2or7pOmJcBHt8Ya
"""

buffer = int(input('Enter buffer size'))

sequence = list(map(int, input('Enter input sequence').split()))


buffer_ls = []
page_fault = 0

for val in sequence:
    idx = []
    tmp_ls = sequence[sequence.index(val)+1:]
    
    if len(buffer_ls)<buffer:
        if val in buffer_ls:
            print('--hit--')
        else:
            page_fault+=1
            buffer_ls.append(val)
            print(buffer_ls)
    else:
        if val in buffer_ls:
            print('--hit--')
        else:
            page_fault+=1
            
            for i in buffer_ls:
                try:
                    idx.append(tmp_ls.index(i))
                except:
                    continue    
            
            buffer_ls.remove(tmp_ls[max(idx)])
            buffer_ls.append(val)
            print(buffer_ls)
print('Number of page fault', page_fault)
# -*- coding: utf-8 -*-
import csv
reader=csv.reader(open('tennis.csv','r'))
your_list=list(reader)
h=['0','0','0','0','0','0']
for i in your_list:
    if i[-1]=="TRUE":
        j=0
        for x in i:
            if x!="TRUE":
                if x!=h[j] and h[j]=='0':
                    h[j]=x
                elif x!=h[j] and h[j]!='0':
                    h[j]='?'
                else:
                    pass
                j=j+1
print("most specific hypothesis is")
print(h)                    

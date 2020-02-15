'''
zip() function workes in sets lists dictionary
it is mainly used in dictionary
'''


a=[1,2,3]
b=[22,66,99]
d=[11,12,13]
c=e=list(zip(a,b,d))
e=set(zip(a,b,d))
print(e)
print(c)
print(c[2][1])
di=e=dict(zip(a,b))     # dictionary is key value pair so we can merge only 2 lists
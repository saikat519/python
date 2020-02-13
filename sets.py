'''
sets in python is same as math
it's denoted with {} as an example:- s={}
1)sets are immutable it means assignment operation would not work here after once the value assigned once
2) repeatation in one set is not allowed
3) we can easily typecast sets into list
'''

s1={11,22,33,11,88}
s2={33,22,88,44,99}
print(s1)
print(s2)

print(s1-s2)        # same as difference between two sets or we can say intersection of two sets

print(s1 | s2)        # concatination of two sets without repeatation of any value

print(s1 & s2)      # values which are repeating in s1  and  s2

print(s1 ^ s2)      #values which are not repeating in s1  and  s2

print(s1[1])        # not fetchable

s1[1]=12
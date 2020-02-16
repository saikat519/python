# Taking set input dynamically::
s={}
print(type(s))
s={int(i) for i in input('Enter::').split()}
print(s)
print(type(s))


# Set builtin function::
s1={11,12,31,45,4}
s1.add(19)
print('add function::')
print(s1)       # add(x) adds x in set unorderly
s1.remove(12)
print("remove function:: ")
print(s1)
print('pop retrns:',s1.pop())
print('pop function::')
print(s1)
s2={11,45,19,32}
print("difference function")
print(s1.difference(s2))        # s1-s2
print('intersection::')
print(s1.intersection(s2))
print('Union')
print(s1.union(s2))
print('Discard::')
s1.discard(11)
print(s1)
print(s1.symmetric_difference(s2))              # prints only non repeating items of s1 and s2
s3={12,45,30,32}
s3.difference_update(s2)
print(s3)                       # s3=s3-s2

print('isdisjoint Function::')
s4={1,2,11,33}
s5={22,44,55,66}
print(s4.isdisjoint(s5))        #returns boolean value True if s4 != s5

print('clear Function::')
s3.clear()
print(s3)

print("subset & superset::")
set1={1,2,3,4,5}
set2={2,3,4}
set3={2,3,9}
print('superset::')
print(set1.issuperset(set2))        # if the set2 elements are present in set1 then set2 is a superset of set1
print(set1.issuperset(set3))

print('subset::')
print(set2.issubset(set1))
print(set3.issubset(set1))

print('update function::')
print(set1)
set3={1,2,11,44}
print(set3)
set1.update(set3)
print(set1)
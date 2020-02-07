'''taking inputs in a list
by default input() returns string so we have to type cast according to our preference
a=[]
n=int(input("Range::"))
for i in range(n):
    a.append(input())
print(a)

'''
a=[1,2,2.5,True,'saikat']           #lists in python are mutable,supports multiple datatype in a singular list
print(a)

''' indedxing in list:::
python list indexing start with 0 by default
it supports -ve indexing also

'''

print(a[-1])        #-ve indexing starts from last index and ends at a[0] i.e a[4]=a[-1]
print(a[4])         #verify


#List slicing

print(a[:])         # prints each and everything exists in the list
print(a[0:5])       # Before : part is inclusive and After : is exclusive
print(a[1:4])

# mutable and easily accessable

print(a[3])         # we can access easily
a[3]=False
print(a[3])         #we can change the value if we know the position

# nested lists

b=[[99,[12,13]],[1,2,3,4,5]]
print(b[0][1][0])               # it means 0'th element's  -> 1st element's -> 0'th element
                                #      ||                        ||              ||
                                # [99,[12,13]]            ->  [12,13]       ->  12
#suppose we wanna access 2 from b[]
print(b[1][1])


# inbuilt function in list

arr=[1,2.5,'saikat',True]

arr.append('Python')
print(arr)

co=arr.copy()           #copies whole list
print('hehe',co)

print(arr.pop())        #deletes last element of the list stack based data structure
print(arr)

arr.extend('saikat')
print(arr)

arr.extend(["saikat","ribu",108])
print(arr)

arr.reverse()
print(arr)      # reverse the list


print(arr.count("a"))    # counts the no of searched elements present in the list
print(arr.index('ribu'))    # counts the index number of element present in the list

del(arr[:])
print(arr)


ab=[1,2,44]
ab.clear()                      # arr.clear() is equivalent of del(arr[:])
print(ab)                       # both deletes every item from the list


abc=[33,333,1,4,7,77,8,99]

abc.sort()    # By default in sort() reverse=False if we want to sort in reverse order we need to set it into True
print(abc)

# to sort in reverse order


abc.sort(reverse=True)
print(abc)

#length of a list::: returns human calculative length starts from 1 NOT from 0

print(len(abc))


# insert()

abc.insert(2,333)       # a.insert(index,element)
print(abc)

abc.remove(333)     #remove(x) removes first value of x from the left of the list
print(abc)


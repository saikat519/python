from operator import itemgetter

students=[['vivek', 'B', 45], ['adi', 'A', 30], ['Tirtha', 'C', 2]]

b=sorted(students,key=itemgetter(2,0)) # According roll then name
print(b)

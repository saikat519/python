s=input('string::')
arr=list(s)

for i in range(len(arr)):

    if arr[i] >= 'A' and arr[i] <= 'Z':
        arr[i]= arr[i].lower()
    elif arr[i] >= 'a' and arr[i] <= 'z':
        arr[i] = arr[i].upper()
    else:
        pass

str=""

for x in arr:
    str+=x
print(str)
'''
def swap_case(s):
    return s.swapcase() -->case changer function
s=input('String::')
result=swap_case(s)
print(result)
'''
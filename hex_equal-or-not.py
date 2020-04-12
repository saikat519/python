'''
input :
first line contains a hexadecimal value
secondline contains a decimal value

output:
check if they equal or not
'''



h=input('Enter a Hexadecimal NUM:')
k=int(input('Enter a decimal number:'))
deci=int(h,16)      # To convert hexa to a decimal number
if deci==k:
    print('Equal')
else:
    print('Not Equal')
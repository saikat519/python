'''
if a number divisable by 3 print Fizz
if the number divisable by 5 print Buzz
if the number divisable by 3 and 5 both print FizzBuzz


'''
n=int(input('Enter a Num:::'))

if n%3==0 and n%5!=0:
    print('Fizz')
elif n%5==0 and n%3!=0:
    print('Buzz')
elif n%15==0:
    print('FizzBuzz')
else:
    pass
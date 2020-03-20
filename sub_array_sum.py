def SubArray(arr,s,n):
    for i in range(n):
        curr_sum=arr[i]

        for j in range(i+1,n):
            if(curr_sum==s):
                print(i,j-1)          # Bcz if condition is before the summing operation
                return 1

            curr_sum = curr_sum+arr[j]      # summing operation

    print('no SubArray found:')


t=int(input('number of test cases:::'))
for k in range(t):
    n,s=input("num of elements,sum::").split()
    n=int(n)
    s=int(s)
    arr=[int(i) for i in input().split()]
    SubArray(arr,s,n)

'''
suppose the sum is 33 and the array is: [1 2 10 3 20 5]
so when i pointing to 10
then j starts from 3 upto 5
when curr_sum=10+3
i pointing to 10 and j is pointing 3
next time again i pointing 10 and j pointing 20
when next time itterates j is pointing 5 bcz for loop is incrementing j value
and then if conditon satisfies..... then return
so when we have to print the sub array's index j must be decremented by 1
bcz j is pointing at 5 But the correct index is  2-4
so, i will remain same and j must be j=j-1
so, print(i,j-1) 

'''
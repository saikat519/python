def gcd(a,b):
    if a==0:
        return b
    if b==0:
        return a
    else:
        return gcd(b%a,a)
def lcm(a,b):
    return (a*b)//gcd(a,b)

a=15
b=20
print(gcd(a,b))
print(lcm(a,b))
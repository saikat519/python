s=input('Enter a String::')
s1=[]
for i in range(len(s)-1,-1,-1):
    if s[i].isalpha()==True:
        s1.append(s[i])

for j in range(len(s)):
    if s[j].isalpha()==False:
        s1.insert(j,s[j])
print(''.join(s1))

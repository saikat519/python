def count_repeat(sen):
    arr=[]
    d={}
    for ele in sen:
        if ele in d:
            d[ele]+=1
        else:
            d[ele]=1
            arr.append(ele)
    for ele in arr:
        if d[ele]==1:
            return ele
    return None

sentence=input('Enter a string:')
result=count_repeat(sentence)
if result==None:
    print('There are all reapeating char in sentence:')
else:
    print('first non repeating element is:: {}'.format(result))
'''
Public Test Cases:
Input:
Python
Output:
Python1

Input:
Java0009
Output:
Java0010

Private Test Cases:
Input:
C++099
Output:
C++100

Input:
C00599
Output:
C00600

Input:
R09999
Output:
R10000

'''
#String increment
s=input()
n=''
q=''
for i in s:
    if i.isdigit():
        n+=i
    else:
        q+=i
if n=='':
    q+='1'
else:
    a=int(n)
    a=a+1
    ns=str(a)
    n=list(n)
    ns=list(ns)
    for i in range(1,len(ns)+1):
        n[-i]=ns[-i]
        f=''
    for i in range(len(n)):
        f+=n[i]
    q=q+f
print(q)

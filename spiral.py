'''n=4
mat=[]
for i in range(n):
    l=[]
    for j in range(n):
        x=int(input())
        l.append(x)
    mat.append(l)
z=[[0]*n]*n]
for k in range(n):
    for s in range(n):
        if k==0:

            z[0][k

from collections import Counter
n=int(input())
b=bin(n)
b=b[2:]
l=[]
for i in b:
    l.append(i)
c=Counter(l)
leg=len(l)
if c['1']==1:
    print("Yes")
else:
    print("NO")
n=int(input())
sqn=n**0.5

print(sqn)
for i in range(2sqn)//2)+1):
    if sqn%i==0:
        f=0
        break
    else:
        f=1
if f==1:
    print("Yes")
else:
    print("No")

def isHappy(n):
        """
        :type n: int
        :rtype: bool
        """
        if n==1:
            return True
            exit()
        s=str(n)
        sq=s
        f=0
        while(int(sq)>1):
            print(sq)
            f=0
            for i in range(len(sq)):
                f=f+(int(sq[i])**2)
            sq=str(f)
            
        if f==1:
            return True
        else:
            return False

r=isHappy(123)
print(r)'''





def countSubarrays(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=nums
        c=0
        for i in range(len(nums)):
            if i<len(nums)-2:
                if (l[i]+l[i+2])== (l[i+1])/2:
                    c+=1
        return c
nums=[2,-7,-6]
print(countSubarrays(nums))









a=2
b=-6
print(a+b)

















'''
Sample Input:
apple
Sample Output:
zkkov
Explanation:
a->z
p->k
p->k
l->o
e->v

Test Case 1
Input:
Instacks
Output:
Rmhgzxph

Test Case 2
Input:
We were passing notes
Output:
Dv dviv kzhhrmt mlgvh

Test Case 3
Input:
Hello World!
Output:
Svool Dliow!

Test Case 4
Input:
Christmas is the 25th of December
Output:
Xsirhgnzhrhgsv 25gs luWvxvnyvi

'''
s=input()
l=list(s)
f=''
a='abcdefghijklmnopqrstuvwxyz'
A='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
sc="!@#$%^&*()> <?/|\'"
for i in l:
    if i.isdigit():
        f+=i
    if i in sc:
        f+=i
    if i.isalpha():
        if i in a:
            c_i=a.index(i)
            f+=a[-(c_i+1)]
        if i in A:
            c_i=A.index(i)
            f+=A[-(c_i+1)]
            
print(f)

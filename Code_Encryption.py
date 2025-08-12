#reverse the string and replace
s=input()
s=s[::-1]
vow='aeiou'
dig='01223'
f=''
#apple
#elppa
for i in s:
    if i not in vow:
        f+=i
    else:
        c_i=vow.find(i)
        f+=dig[c_i]
f=f+'aca'
print(f)
'''

Public Test Cases:
Input:
banana
Output:
0n0n0baca

Input:
apple
Output:
1lpp0aca

Input:
hello
Output:
2ll1haca

Private Test Cases:
Input:
karaca
Output:
0c0r0kaca

Input:
burak
Output:
k0r3baca

Input:
alpaca
Output:
0c0pl0aca

Input:
Instacks
Output:
skc0tsnIaca

Input:
crypt
Output:
tpyrcaca


'''

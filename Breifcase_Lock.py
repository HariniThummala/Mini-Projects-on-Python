'''
Sample Input:
4089
5672
Sample Output:
9
Explanation:
1st Number is the Old Password
2nd Number is the New Password

1st Number change:
4 ➞ 5
Forward Turns: 1 <- Min
4 ➞ 5
Backward Turns: 9
4 ➞ 3 ➞ 2 ➞ 1 ➞ 0 ➞ 9 ➞ 8 ➞ 7 ➞ 6 ➞ 5

2nd Number Change
0 ➞ 6
Forward Turns: 6
0 ➞ 1 ➞ 2 ➞ 3 ➞ 4 ➞ 5 ➞ 6
Backward Turns: 4 <- Min
0 ➞ 9 ➞ 8 ➞ 7 ➞ 6

3rd Number Change
8 ➞ 7
Forward Turns: 9
8 ➞ 9 ➞ 0 ➞ 1 ➞ 2 ➞ 3 ➞ 4 ➞ 5 ➞ 6 ➞ 7
Backward Turns: 1 <- Min
8 ➞ 7

4th Number Change
9 ➞ 2
Forward Turns: 3 <- Min
9 ➞ 0 ➞ 1 ➞ 2
Backward Turns: 7
9 ➞ 8 ➞ 7 ➞ 6 ➞ 5 ➞ 4 ➞ 3 ➞ 2

Total Turns –
1+4+1+3 = 9

'''
pre=input()
post=input()
lp1=list(str(pre))
lp2=list(str(post))
'''
4089
5672
['4', '0', '8', '9']
['5', '6', '7', '2']

'''
t=0
for i in range(4):
    if int(lp1[i])==int(lp2[i]):
        continue
    else:
        d=abs(int(lp1[i])-int(lp2[i]))
        if d<=5:
            t+=d
        if d>=6:
            if int(lp1[i])>int(lp2[i]):
                d=10-int(lp1[i])
                t+=d+1
            if int(lp2[i])>int(lp1[i]):
                d=10-int(lp2[i])
                t+=d+1
            
print(t)

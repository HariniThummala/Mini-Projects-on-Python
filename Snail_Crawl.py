d=int(input())
f=0
m=0
for i in range(1,d):
    f=f+5
    m=m+1
    if f==d or f>d:
        print(m)
        break
    if i%30==0:
        m+=10
        f=f-30
            

    
    
    

    

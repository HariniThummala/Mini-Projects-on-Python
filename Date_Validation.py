def date_validation(dat):
    d,m,y=dat.split('/')
    if int(d)>31 or int(d)<=0:
        print("Date is Invalid")
        return
    if int(m)>12 or int(m)<=0:
        print("Month is Invalid")
        return
    if int(y)<1900 or int(y)>9999:
        print("Year is Invalid")
        return
    if (int(y) %4==0 and int(y)%100!=0) or (int(y)%4==0 and int(y)%400==0):
        l=1
        md={1:31,2:29,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
    else:
        md={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
    if md[int(m)]>=int(d):
        print("Entered Date is Valid")
    else:
        print("Date is Invalid")
dat=input("Enter the Date in DD/MM/YY Format:")
date_validation(dat)

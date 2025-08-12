up={'harini':'H@rini1208','jaya':'J@ya1004','anitha':'Anith@1206'}
kart={}
def login():
    user=input("enter username:")
    if user in up:
        pas=input("enter password:")
        if up[user]==pas:
            print()
            print()
            print("*************************************************************")
            print("Log in Successfully!!!!")
            print("*************************************************************")
            print()
            print("Shopping Kart Management")
            print("1.Add Item\n2.View Cart\n3.Delete Item\n4.Calculate Total\n5.exit")
            print()
            print("Items Available:")
            print("1.dress\n2.shirt\n3.vegetables")
            print()
            print("*************************************************************")
        else:
            print("Invalid password")
            print("Enter again")
            login()
    else:
        print("Invalid  user name ")
        login()
        
def signup():
    user=input("Enter corect user name:")
    if user in up:
        print("Username already exists")
        signup()
    else:
        pas=input("Enter correct passs")
        r=pass_validation(pas)
        if r==1:
            up[user]=pas
            print()
            print()
            print("*************************************************************")
            print("Registered Successfully!!!!")
            print("*************************************************************")
            print()

            print("Shopping Kart Management")
            print("1.Add Item\n2.View Cart\n3.Delete Item\n4.Calculate Total\n5.exit")
            print()
            print("Items Available\n")
            print("1.dress\n2.shirt\n3.vegetables")
            print()
            print("*************************************************************")
        else:
            print("Try new Password")
            signup()
def pass_validation(pas):
    if len(pas)<4:
        return 0
    dc=0
    u=0
    l=0
    s=0
    for i in pas:
        if i.isdigit():
            dc+=1
        if i.isupper():
            u+=1
        if i.islower():
            l+=1
        if i in '!@#$%^&*()?/':
            s+=1
    if dc>0 and u>0 and l>0 and s>0:
        return 1
    else:
        return 0
def add_item(i_name,i_quan,i_p):
    if i_name  not in kart:
        kart[i_name]=[i_quan,i_p*i_quan]
        print(f"Item {i_name} added Successfully!!")
    else:
        cur_q,cur_p=kart[i_name]
        kart[i_name]=[cur_q+i_quan,cur_p+(i_quan*i_p)]
        print(f"Item {i_name} added Successfully!!")

def display(kart):
    print(kart)
def cal_tot(kart):
    t=0
    for i in kart.values():#{{'dress':[2,2000]},{'shirt':2,1000}}
        t+=i[1]
    print(f"Total Amount is:    {t}")
def del_item(i_name,i_quan,i_p):
    if i_name not in kart:
        print("Item is not available in your Kart:")
        return
    else:
        cur_q,cur_p=kart[i_name]
        kart[i_name]=[cur_q-i_quan,cur_p-(i_quan*i_p)]
        print(f"Item {i_name} removed Successfully!!")
print("*********************************************************")
print("Welcome to Shopping Kart!")
print("*********************************************************")
print("1.Login if account is already exists")
print("2.Sign up if account is not already exist")
print("*********************************************************")
c=input("Login/Signup[l/s]?")
if c=='l':
    login()
if c=='s':
    signup()
while(True):
    sel=int(input("select operation:"))
    if sel==1:
        i_name=input("Enter item name to add into kart:")
        i_quan=int(input("Enter Quantity:"))
        i_p=int(input("Enter Price:"))
        add_item(i_name,i_quan,i_p)
    if sel==2:
        display(kart)
    if sel==3:
        i_name=input("Enter an item to delete from kart:")
        i_quan=int(input("Enter quantity:"))
        i_p=int(input("Enter price:"))
        del_item(i_name,i_quan,i_p) 
    if sel==4:
        cal_tot(kart)
    if sel==5:
        print("You are out of the Cart!!!")
        exit()
    if sel>5 or sel<=0:
        print("Enter correct operation")
        
    
        


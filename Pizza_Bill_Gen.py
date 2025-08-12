import random
from datetime import datetime
bn=random.randint(10000,99999)
dt=datetime.now().strftime("%y-%m-%d %H:%M:%S")
print()
#category
print("Pizza Categories\n1.Regular\n2.Special")
cat=int(input("Enter your Choice[1 or 2]:"))
print()
#type
print("Pizza Type\n1.Veg\n2.Non-Veg")
typ=int(input("Enter your Choice[1 or 2]:"))
print()
#setting prices
if cat==1 and typ==1:
  base=300
elif cat==1 and typ==2:
  base=400
elif cat==2 and typ==1:
  base=600
elif cat==2 and typ==2:
  base=800
else:
  print("Incorrect option chosen")
total=base
#Add ons
addons=['Extra Cheese','Extra Topping','Water Bottle','Ketchup','Soft Drinks','Take away charges']
prices=[100,100,30,5,75,20]
final=[]
for i in range(len(addons)):
  x=int(input(f"{addons[i]}?[1.yes 2.no]"))
  if x==1:
    q=int(input("Enter Quantity:"))
  else:
    q=0
  print(f"{addons[i]}cost is:{q*prices[i]}")
  total+=q*prices[i]
  final.append(q*prices[i])
print(f"Total cost is:{total}")
print()
print("********************************************")
print("************Pizza Bill Generator************")
print("********************************************")
print(f"Bill Number             :{bn}")
print(f"Date and Time           :{dt}")
print("********************************************")
print(f"Base Price              :{base}")
for i in range(len(addons)):
  if final[i]!=0:
    print(f"{addons[i]}            :{final[i]}")
print("********************************************")
print(f"Total Cost              :{total}")
print(f"GST Charges             :{round((total*0.16),2)}")
print("********************************************")
print(f"Net Amount Payable      :{total+(total*0.16)}")
print("********************************************")


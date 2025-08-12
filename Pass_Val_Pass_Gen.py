def pass_suggestion():
  from random import choice
  u=[chr(i)for i in range(65,91)]
  l=[chr(i)for i in range(97,123)]
  d=[chr(i)for i in range(48,58)]
  s="!@$%^&*()_+?<>"
  pas=choice(u)+choice(l)+choice(d)+choice(s)+choice(u)+choice(l)+choice(d)+choice(s)
  return pas
def pass_validation(pw):
  u=[chr(i)for i in range(65,91)]
  l=[chr(i)for i in range(97,123)]
  d=[chr(i)for i in range(48,58)]
  s="!@$%^&*()_+?<>"
  uc=0
  lc=0
  dc=0
  sc=0
  if len(pw)<8:
    print("Password should be atleast 8 characters long")
    print("Do you want password suggestion {y/n}")
    c=input()
    if c=='y':
      pw=pass_suggestion()
      print(pw)
    exit()
  else:
    for i in pw:
      if i in u:
        uc+=1
      elif i in l:
        lc+=1
      elif i in d:
        dc+=1
      elif i in s:
        sc+=1
    if uc!=0 and lc!=0 and dc!=0 and sc!=0:
      print(pw)
      exit()
    else:
      print("Password is invalid")
      print("Do you want password suggestion {y/n}")
      c=input()
      if c=='y':
          pw=pass_suggestion()
          print(pw)
          exit()
username=input("Please enter user name:")
password=input("Please enter user password:")
pass_validation(password)

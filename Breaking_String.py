s=input("Enter the String:")
print("String Information's is as follows:")
print(f"String Length       :{len(s)}")
ta=0
ua=0
la=0
v=0
c=0
d=0
sc=0
vow='aeiouAEIOU'
scr='!@#$%^.&*()_+-=<>?}{[]'
for i in s:
    if i.isalpha():
        ta+=1
        if i.islower():
            la+=1
            if i in vow:
                v+=1
            else:
                c+=1
        if i.isupper():
            ua+=1
            if i in vow:
                v+=1
            else:
                c+=1
    if i.isdigit():
        d+=1
    if i in scr:
        sc+=1
print(f"Total Alphabets     :{ta}")
print(f"Uppercase Alphabets :{ua}")
print(f"Lowercase Alphabets :{la}")
print(f"Vowels              :{v}")
print(f"Consonants          :{c}")
print(f"Digits              :{d}")
print(f"Special Characters  :{sc}")

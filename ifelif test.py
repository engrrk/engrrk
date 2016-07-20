s = "hello world!123"
l=0
d=0
for char in s:
    if char.isalpha():
        l = l+1
    elif char.isdigit():
        d=d+1
print("letters :" + str(l) + "\n digits " + str(d)+".")
num=int(input("Enter a whole number:"))
c=0
t=num
if num <= 9 and num >= 0:
    c=1
    print(c)
else:
    while t > 0:
        c+=1
        t //=10
print("The length of", num, "is", c)
x=int(input("enter the value  to find"))
for i in range(2,x):
    for j in range(2,i):
        if i%j==0:
            break
        
    else:
        print(i)

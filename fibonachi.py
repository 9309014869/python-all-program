x=int(input("enter the value  to find"))
m=0
n=1 
for i in range(1,x):
    if i==0 or i==1:
      print(m)
      print(n)
    else:
      c=m+n   
      m=n
      n=c
      print(c)
        

x,y,z=map(int,input().split())
if x>y and x>z:
    if y>z:
        print("the secound greatest",y)
if y>x and y>z:
    if z>x:
        print("the secound greatest",z)
if z>y and z>x:
    if x>y:
        print("the secound",y)

import array as arr
a=arr.array('i',[1,3,7,8])
print(len(a))
a.append(8)
print(a)
a.extend([8,9,11,78])
print(a)
a.insert(8,9)
print(a)

print(a.pop())
print(a)
for i in range(0,len(a)):
    print(a[i])
    

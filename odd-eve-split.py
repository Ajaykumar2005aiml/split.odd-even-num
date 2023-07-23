a=list(map(int,input()))
b=len(a)
c=[]
d=[]
for i in range(0,b):
  if a[i]%2==0:
    c.append(a[i])
  else:
    d.append(a[i])
c.sort()
d.sort()
print(*c)
print(*d)

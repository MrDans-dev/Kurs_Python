import numpy as np
a = np.arange(1,7)
b = np.arange(1,7).reshape(2,3)
m = np.arange(2,51,2)
m=m.reshape(5,5)
print(m)
print(m.T)
print(m.T**2)
print(m.T+np.diag(np.ones(5)))
c = np.diag([5 for i in range(5)])
print(c)
print(a)
a=a.reshape(2,3)
print()
print(a)
for i in range(3):
    print(a[:,i],np.min(a[:,i]))
for i in range(2):
    print(a[i,:])
print()
for i in a.flat:
    print(i)
print(type(a))
print(a.T)
print(a*b)
#print(a.reshape(6))
#print(a.flat)

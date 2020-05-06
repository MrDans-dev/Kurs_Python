import numpy as np
a = np.arange(1,7)
b = np.arange(1,7).reshape(2,3)
print(a)
for i in a:
    print(i)
a=a.reshape(2,3)
for i in a.flat:
    print(i)
print(type(a))
print(a.T)
print(a*b)
#print(a.reshape(6))
#print(a.flat)

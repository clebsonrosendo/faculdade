import numpy as np


arr = np.array([1, 2, 3, 4])
x=arr.copy()
y=arr.view()

x[0]=42
y[0]=43

print(arr)
print(x)
print(y)

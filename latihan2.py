import numpy as np

b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(b)
print("=====================")
print(c)
print("=====================")
print(d)
print("=====================")
print(b.ndim)
print(c.ndim)
print(d.ndim)
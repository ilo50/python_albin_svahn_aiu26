import numpy as np, matplotlib.pyplot as plt

r = range(-10, 10)

l = list(r)

number_array = np.array(r)

print(l[0])

x = np.linspace(-3,3, 50)
print(x)

y = -x**2

plt.plot(x,y)
#plt.show()

# 2d array

table = [[1,2,43,42], [-3,5,8,3]]

for row in table:
    print(row)

matrix = np.array(table)
print(matrix)
print(matrix.shape)

print(matrix.T)
print(matrix.T[:,0])


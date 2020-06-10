import numpy as np
from matplotlib import pyplot as plt

# print(np.arange(5))
#
# L = list(range(10))
# # Create a 3*5 array filled with 3.14
# print(np.full((3, 5), 3.14))
#
# # Create an array filled with a linear sequence
# # Starting at 0, end at 20, stepping by 2
# print(np.arange(0, 20, 2))
#
# # create an array of five values evenly spaced between 0 and 1
# print(np.linspace(0, 1, 5))

# # Create a 3*3 array of uniformly distributed random value between 0 and 1
# print(np.random.random((3, 3)))
#
# # Create a 3*3 array of normally distributed random value with mean 0 and standard deviation 1
# print(np.random.normal(0, 1, (3, 3)))
#
# # Create a 3*3 array of random integers in the interval [0,10]
# print(np.random.randint(0, 10, (3, 3)))
#
# # Create a 3*3 identity metrix
# print(np.eye(3))

np.random.seed(0)

x1 = np.random.randint(10, size=6)
x2 = np.random.randint(10, size=(3, 4))
x3 = np.random.randint(10, size=(3, 4, 5))

print(x2)
# print(x2[2, 2])

# print(x3)
# # Accessing single element
# print(x3[0, 2, 4])

# Slicing

# print(x2[:3, ::2])

# # Iterate array
# for x in np.nditer(x3):
#     print(x)

# x = np.arange(1, 11)
# y = 2 * x + 5
# plt.title("Matplotlib demo")
# plt.xlabel("x axis caption")
# plt.ylabel("y axis caption")
# plt.plot(x, y)
# plt.show()

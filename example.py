import numpy as np 
import matplotlib.pyplot as plt
x = input("Enter name here: ")

print('hello' + x)


y = np.array([i for i in range(20)])
y2 = 2*y

plt.plot(y,y2)
plt.savefig('test.png')



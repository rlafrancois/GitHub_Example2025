import numpy as np 
import matplotlib.pyplot as plt
x = input("Enter name here: ")
#Printing name provided as input
print('hello' + x)


y = np.array([i for i in range(20)])
y2 = 2*y

plt.plot(y,y2)
plt.savefig('test.png')
#This is a comment for a enw feature
#Enter new feature here
#Additional comments
#remember to delete this comment
#delete this as well
####


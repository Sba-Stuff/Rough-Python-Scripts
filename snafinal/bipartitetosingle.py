import numpy as np
a1 = np.array([[1,0,0,0],
[1,0,0,0],
[1,1,0,0],
[1,1,1,1],
[0,0,0,1]])
#print(a1)
#print(np.transpose(a1))
print(np.dot(a1,np.transpose(a1)))
import numpy as np
a1 = np.array([[0,1,0,1],
[0,0,1,1],
[1,0,0,0],
[0,0,1,0]])
a2 = np.array([2,6,4,3])
#print(a1)
#print(np.transpose(a1))
print(np.dot(a1,a2))
import numpy as np
a1 = np.array([[0,1,0,1],
[0,0,1,1],
[1,0,0,0],
[0,0,1,0]])
a2 = np.array([9,7,2,4])
#print(a1)
#print(np.transpose(a1))
print(np.dot(np.transpose(a1),a2))
import numpy as np
a1 = np.array([[0,1,1],
[1,0,0],
[0,1,1]])
a2 = np.array([2,1,3])
#print(a1)
#print(np.transpose(a1))
print(np.dot(np.transpose(a1),a2))


import numpy as np
a1 = np.array([[0,.5,.5],
[1,0,0],
[0,1,0]])
a2 = np.array([1/2,1/4,1/4])
#print(a1)
#print(np.transpose(a1))
print(np.dot(np.transpose(a1),a2))
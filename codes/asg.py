import numpy as np

#making matrix
A = np.matrix('[2,4; 3,5]')

#finding tA
tA = A.transpose()

#adding A and tA
R = np.add(A,tA)

#finding tR
tR = R.transpose()

#to check R is symmetric
if np.array_equal(R,tR):
    print("the matrix is symmetric")
else:
    print("the matrix is not symmetric")
    



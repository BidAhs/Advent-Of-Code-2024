import re
import numpy as np

with open('dayFourInput.txt','r') as f:
    matrix =np.array([list(l.strip()) for l in f])

m,n = matrix.shape
isSM = lambda mat: {mat[0,0], mat[2,2]} == {'S','M'} and {mat[0,2], mat[2,0]} == {'S','M'}

res = sum(1 for i in range(1,m-1) for j in range(1,n-1) if matrix[i,j]=='A' and isSM(matrix[i-1:i+2,j-1:j+2]))
print(res)

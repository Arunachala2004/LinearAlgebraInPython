#importing required library
import numpy as np
#illustrative a Zero row vector of dimension 3 using np.array() function
zeroRowVector1=np.array([0,0,0])
print(zeroRowVector1)

#Illustrative a zero row vector of dimension 3 using np.zeros() function
zeroRowVector2=np.zeros(3)
print(zeroRowVector2)

#Illustrative a zero column vector of dimension 3 using np.zeros() and reshape() function
zeroVector3=np.zeros(3).reshape(3,1)
print(zeroVector3)

import numpy as NP
vector=NP.array([[1],[-2],[4]])
print("The vector\n", vector)
print("\nElements at position",1,"is",vector[1])
print("\nElements at position",2,"is",vector[2])
try:
    print("\nElements at position",3,"is",vector[3])
except:
    print("\nElements at position specified above is not there (Dimensional Error)")
print("\nElements at position",0,"is",vector[0])


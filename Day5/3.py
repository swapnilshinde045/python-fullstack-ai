import numpy as np

s=np.array([[80,70,90],[60,85,75]])

print(s.sum())
print(s.mean())
print(s.max())
print(s.min())
print(s.argmax())

print(s.sum(axis=0)) #column wise
print(s.sum(axis=1)) #row wise

print(s + np.array([5,5,5])) #broadcasted addition

col= np.array([[1],[2]])
row= np.array([10, 20, 30])

print(col + row) # broadcasted addition


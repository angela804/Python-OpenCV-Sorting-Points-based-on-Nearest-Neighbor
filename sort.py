import numpy as np 
x = []
y = []
dataset = []

for t in range(len(x)):
    dataset.append(x[t],y[t])

dataset.sort(key=lambda x:x[0])
dataset = np.array(dataset)
dataset = sorted(dataset, key = lambda point: euclidian_distance(point,dataset[0]))

def euclidian_distance(self, a,b):
    return np.linalg.norm(a-b)
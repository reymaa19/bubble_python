import numpy as np
np.random.seed(1)

SIZE = 100
MAX = 100

def bubble(data):
    for i in range(len(data)-1):
        if data[i] > data[i+1]:
            temp = data[i]
            data[i] = data[i+1]
            data[i+1] = temp

def repeat(data):
    for i in range(len(data)-1):
        bubble(data)

data = np.random.randint(0 ,MAX+1, SIZE)

repeat(data)
print(data)
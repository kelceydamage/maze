import numpy as np 

temp = np.zeros((4, 4))
test = np.zeros((4, 4))
rand = np.random.normal(0, 1, size=(4, 4))

test[rand > 0.5] = 1

print(test)
indices = np.nonzero(test)

#v = np.stack(indices, axis=-1)

print(indices)

print(test[indices])

indices = np.nonzero(test == 0)


print(indices)

print(test[indices])
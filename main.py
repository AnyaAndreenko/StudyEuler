import numpy as np

a = np.arange(0, 1000)
t = np.array([])
cumm = 0
for i in range(0, 1000):
    if a[i] % 3 == 0 or a[i] % 5 == 0:
        t = np.append(t, a[i])
        cumm += t[-1]

print(cumm)

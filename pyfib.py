import numpy as np
import matplotlib.pyplot as plt

t1 = np.arange(0, 8, 0.05)
t2 = np.arange(10, 14, 0.05)
t = np.concatenate([t1, t2])
c = [np.cos(i) for i in t]

fig = plt.figure()
ax = fig.gca()
ax.plot(t, c)
ax.set_title('Undesirable joining line')


t1 = np.arange(0, 8, 0.05)
t2 = np.arange(10, 14, 0.05)
c1 = [np.cos(i) for i in t1]
c2 = [np.cos(i) for i in t2]
t = np.concatenate([t1, t1[-1:], t2])
c = np.concatenate([c1, [None,], c2])

fig = plt.figure()
ax = fig.gca()
ax.plot(t, c)
ax.set_title('Ok if you don\'t pan the plot')

fig = plt.figure()
ax = fig.gca()
ax.plot(t, c)
ax.axis([-1, 12, -0.5, 1.25])
ax.set_title('Strange jumping line')

plt.show()

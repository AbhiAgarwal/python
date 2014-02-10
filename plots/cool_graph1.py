import pylab as p
import numpy as np

x = np.arange(0, 1, 0.01)
m = np.arange(48, 55)

y = []

for e in m:
    y.append((2**e + 1)*x - (2**e)*x)
    
p.hold(True)

for fn in y:
    p.plot(x, fn)
    
p.ylim(-0.5, 1.1)
p.show()
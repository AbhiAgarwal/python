import numpy as np
import math as m
import pylab as p
 
i = np.arange(-20,0,0.5)
h = 10.0**i
x0 = 1.2*np.ones(len(i))
f0 = np.sin(x0)
f_neg = np.sin(x0-h)
fp = np.cos(x0)
absolute_forward_error = \
    abs(fp -(np.sin(x0 + h) - f0)/h) 
absolute_central_error = \
    abs(fp - (np.sin(x0 +h) - f_neg)/(2*h))
relative_forward_error = \
    (abs(fp - (np.sin(x0 + h) - f0)/h)) / fp
relative_central_error = \
    (abs(fp - (np.sin(x0 + h) - f_neg)/(2*h))) / fp
forward_true_absolute_error = f0/2*h
forward_true_relative_error = forward_true_absolute_error/fp
central_true_absolute_error = abs(((h**4 / 120.0) - (h**2 / 6.0)) * np.cos(x0))
central_true_relative_error = central_true_absolute_error/fp
 
# plotting
p.hold(True)
# discretization errors
p.loglog(h, forward_true_absolute_error,'b-.',)
p.loglog(h, forward_true_relative_error, 'r-.',)
p.loglog(h, central_true_absolute_error, 'g-.',)
p.loglog(h, central_true_relative_error, 'y-.',)
# actual errors
p.loglog(h, absolute_forward_error,'b-s')
p.loglog(h, absolute_central_error, 'g-s')
p.loglog(h, relative_forward_error, 'r-o')
p.loglog(h, relative_central_error, 'y-o')
 
p.ylim(1e-15, 1e3)
p.xlabel('h')
p.ylabel('Error')
p.title('Forward and central error for $x_0 = 1.2$')
p.show()
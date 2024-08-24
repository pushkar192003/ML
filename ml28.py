import matplotlib.pyplot as plt
import numpy as np

# evenly sampled time at 200ms intervals
t = np.arange(0.0, 5.0, 0.2)  # t = 0.0, 0.2, 0.4, 0.6, 0.8, 1.0.........4.8
print ( t )

# red stars , blue squares and green dots
plt.plot(t, t,   'r*-',
         t, t+3, 'bs-',
         t, t+6, 'r-' ,
         t, t+6, 'go' ,
         markersize=7   )

plt.show()

# t = x = 0.0, 0.2, 0.4, 0.6, 0.8, 1.0.........4.8
# t = y = 0.0, 0.2, 0.4, 0.6, 0.8, 1.0.........4.8
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde

# Generating random sample data
x = np.random.normal(size=1000)
y = np.random.normal(size=1000)

# Performing kernel-density estimation
kde = gaussian_kde(np.vstack([x, y]))

# Generating contours
x_grid, y_grid = np.mgrid[x.min():x.max():100j, y.min():y.max():100j]
positions = np.vstack([x_grid.ravel(), y_grid.ravel()])
z = np.reshape(kde(positions).T, x_grid.shape)

# Plotting the contours
plt.contourf(x_grid, y_grid, z, cmap='Blues')
plt.colorbar()
plt.show()

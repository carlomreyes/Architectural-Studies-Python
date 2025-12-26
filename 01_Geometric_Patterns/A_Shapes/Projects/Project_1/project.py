import numpy as np
import matplotlib.pyplot as plt
r=5
theta = np.linspace(0, 2 * np.pi, 200) #100 points from 0 to 2pi
x= r * np.cos(theta)
y= r * np.sin(theta)
plt.plot(x, y, color="#467E6C") #Plot the circle & set color
plt.axis('equal') #Equal scaling for x and y axes
plt.axis('off') #Turn off the axis
plt.fill(x, y, color="#A3D2CA", alpha=0.5) #Fill the circle with color & transparency
plt.show()
import numpy as np
import matplotlib.pyplot as plt
r=float(input("Enter the radius of the circle: ")) #Radius of the circle
cx=float(input("Enter the center x-coordinate: ")) # Center x-coordinate
cy=float(input("Enter the center y-coordinate: ")) # Center y-coordinate
theta = np.linspace(0, 2 * np.pi, 200) #100 points from 0 to 2pi
x= cx + r * np.cos(theta) #Parametric equation for x
y= cy + r * np.sin(theta) #Parametric equation for y
plt.plot(x, y, color="#2F39C1") #Plot the circle & set color
plt.axis('equal') #Equal scaling for x and y axes
plt.axis('on') #Turn off the axis
plt.fill(x, y, color="#C84C44", alpha=0.1) #Fill the circle with color & transparency
print("Circle drawn with radius:", r) #Print radius to console
print("Circle drawn at center:", (cx, cy)) #Print center coordinates to console
plt.show() #Display the plot

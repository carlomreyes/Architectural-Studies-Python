import numpy as np # For numerical operations
import matplotlib.pyplot as plt # For plotting
a = float(input("Enter the side length of the square: ")) # Enter side length
cx = float(input("Enter the center x-coordinate: ")) # Enter center x-coordinate
cy = float(input("Enter the center y-coordinate: ")) # Enter center y-coordinate
A = a**2 # Area
P = 4 * a # Perimeter
x = [cx - a/2, cx + a/2, cx + a/2, cx - a/2, cx - a/2] # x-coordinates of square vertices
y = [cy - a/2, cy - a/2, cy + a/2, cy + a/2, cy - a/2] # y-coordinates of square vertices
plt.plot(x, y, color="#2F39C1") #Plot the square & set color
plt.fill(x, y, color="#BE2419", alpha=0.1) #Fill the square with color & transparency
plt.axis('equal') #Equal scaling for x and y axes
plt.axis('on') #Turn off the axis
plt.show() #Display the plot
print("Square drawn with side length:", a) #Print side length to console
print("Square drawn at center:", (cx, cy)) #Print center coordinates to console
print("Area of the square:", A) #Print area to console
print("Perimeter of the square:", P) #Print perimeter to console

import matplotlib.pyplot as plt # For plotting
import numpy as np # For numerical operations

custom = input("Specify custom coordinates? (Y/N): ").strip().upper() # Ask user for custom coordinates
if custom == 'Y': # Get custom coordinates from user
    x = float(input("Enter x-coordinate: ")) # Get x-coordinate
    y = float(input("Enter y-coordinate: ")) # Get y-coordinate
else: # Use default coordinates
    x, y = 0, 0 # Default coordinates at origin

POINT_COLOR = "#2F39C1"  # Color of the point
MARKER_SIZE = 100 # Size of the point marker
SHOW_AXES = True # Toggle axis visibility

plt.figure(figsize=(8, 8)) # Create figure
# Plot point (geometric construction)
plt.scatter(x, y, color=POINT_COLOR, s=MARKER_SIZE) # Plot point
plt.axis('equal') # Equal scaling
if SHOW_AXES: # Show or hide axes
    plt.axis('on') # Show axes
else: # Hide axes
    plt.axis('off') # Hide axes
plt.show() # Show plot

print(f"\n{'='*50}") # Separator
print(f"Point plotted at coordinates: ({x}, {y})") # Display coordinates
print(f"Distance from origin: {np.sqrt(x**2 + y**2):.4f}") # Distance from origin
print(f"{'='*50}\n") # Separator
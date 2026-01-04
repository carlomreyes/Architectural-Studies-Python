````markdown
### README.md

# Project 01_1: Basic Circle

This exercise was drafted with the intention of building a simple circle using Python.

## Exercise Requirements:

* Specify **Radius**
* Outline **Color**
* Fill **Color** (optional)
* Axis display (optional)

## Mathematical Foundation:

The project explores the basic geometry of a circle using the **Pythagorean theorem**:

```
x^2 + y^2 = r^2
```

This sets the equation of a circle of radius `r` centered at the origin `(0,0)`. To convert this equation into coordinates suitable for plotting, the **parametric form** is used:

```
x = r * cos(theta), y = r * sin(theta)
```

where `theta` represents the angular parameter (in radians) sweeping the circle, and varies from `0` to `2*pi`.

Vector addition is used to offset the circle’s center from the origin by adding a constant translation vector (cx, cy) to every point on the circle.

```
cx = x-coordinate of the center
cy = y-coordinate of the center
```
This results in a final **parametric form**:

```
x = cx + r * cos(theta), y = cy + r * sin(theta)
```

## Python Implementation:

The script uses `numpy` to generate points and `matplotlib` to plot and optionally fill the circle with color. It also asks the user to input the **radius** and **center coordinates** to make the program interactive:

```
r = float(input("Enter radius of the circle: "))
cx = float(input("Enter the center x-coordinates: "))
cy = float(input("Enter center y-coordinates: "))
```

These values are then used to compute the s=circle’s coordinates and display it graphically.

## Historical Notes:

* The concept of the circle dates back to ancient civilizations (~3000 BCE in Mesopotamia and Egypt) as a fundamental geometric figure.
* Parametric equations and Cartesian coordinates were formalized by **René Descartes in 1637**, allowing mathematical representation of shapes for plotting.
* Python plotting libraries (`matplotlib`) emerged in the early 2000s, inspired by MATLAB, to allow scientific visualization of figures.

## Script Output:

* Colored circle, optionally filled
* Circle center can be translated
* Axis optionally hidden
* Console prints the radius, center coordinates
* User can interactively define the circle’s dimensions and position
````

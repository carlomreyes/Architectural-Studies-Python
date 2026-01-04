````markdown
### README.md

# Project 01_2: Basic Square

This exercise is designed to build a simple square using Python, allowing the user to specify the side length and the center position.

## Exercise Requirements:

* Specify **Side Length** (user input)
* Calculate **Perimeter** and **Area**
* Outline **Color**
* Fill **Color** (optional)
* Axis display (optional)
* Allow translation of the square to any center coordinate `(cx, cy)`

## Mathematical Foundation:

The project explores the basic geometry of a square using its **side length** and the formulas for area and perimeter:

```
Area:      A = a^2
Perimeter: P = 4 * a
```

where `a` is the side length of the square.

Vector addition is applied to offset the square’s center from the origin by adding a translation vector `(cx, cy)` to every corner:

```
cx = x-coordinate of the center
cy = y-coordinate of the center
```

This allows the square to be positioned at any location in the Cartesian plane.

## Python Implementation:

The script uses `numpy` to calculate the coordinates of the square corners and `matplotlib` to plot and optionally fill the square with color. It also asks the user to input the **side length** and **center coordinates** to make the program interactive:

```
a = float(input("Enter side length: "))
cx = float(input("Enter the x-coordinate of center: "))
cy = float(input("Enter the y-coordinate of center: "))
```

These values are then used to compute the square’s coordinates and display it graphically.

## Historical Notes:

* The square is one of the most ancient and fundamental geometric figures, appearing in the architecture and mathematics of early civilizations like Mesopotamia and Egypt (~3000 BCE). It symbolized stability, balance, and order.
* The formal study of square properties, including area and perimeter, was codified in Euclid’s *Elements* (~300 BCE), which provided the foundation for classical geometry.
* The use of parametric equations to define shapes, combined with Cartesian coordinates, became a cornerstone of analytical geometry thanks to René Descartes (1637).
* Modern programming environments such as MATLAB (late 20th century) and Python’s `matplotlib` (early 2000s) have enabled visualizing geometric concepts programmatically, merging historical mathematical theory with computational practice.

## Script Output:

* Colored square, optionally filled
* Square center can be freely translated
* Axis optionally hidden
* Console prints the side length, perimeter, area, and center coordinates
* User can interactively define the square’s dimensions and position
````

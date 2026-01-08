# Project 01_0A: Point

## Overview

This exercise explores the **point** as the most fundamental geometric primitive; a position in space with no dimensions, defined purely by coordinates.

---

## Exercise Requirements

* Prompt user to specify custom coordinates or use default position `(0, 0)`
* If custom: request `x` and `y` coordinate values
* Plot colored point in Cartesian coordinate space
* Optional axis display
* Print confirmation: `"Point plotted at coordinates: (x, y)"`

## Mathematical Foundation

The **point** represents **position with zero dimensions**:
- Cartesian representation: P = (x, y)
- Two degrees of freedom (x, y are independent parameters)
- Foundation for all geometric constructions

**Architectural significance**: Location markers, control points, grid intersections, survey references

---

## Python Implementation

**Computational pipeline**:
```
TOOLS (matplotlib, numpy) 
→ INTENT (coordinates: custom or default) 
→ RULES (conditional: Y/N logic) 
→ FORM (plotted point) 
→ FEEDBACK (console output)
```

**Variable roles**:
- **Input Parameters**: User response (Y/N), coordinates (x, y)
- **Model Parameters**: Default position (0, 0), point color, marker size
- **Constants**: Color codes, axis settings

---

## Historical Context

- **Descriptive geometry** (Monge, 1795): Points as fundamental geometric elements
- **Surveying tradition**: Datum points and reference markers
- **Contemporary practice**: Point clouds (LiDAR), control points (NURBS), grid intersections (BIM)

---

## Script Output

* Colored point marker
* Optional coordinate axes and grid
* Console confirmation with plotted coordinates
* Interactive coordinate specification

---

## Cross-Platform Transfer

| Platform | Point Construction | Parameter Control |
|----------|-------------------|-------------------|
| **Python** | `plt.scatter(x, y)` | Variables: x, y |
| **Grasshopper** | Construct Point component | Number sliders |
| **Dynamo** | Point.ByCoordinates | Number nodes |

**Key concept**: Two independent parameters (x, y) define point position across all platforms

---

## Extension Possibilities

- **Next in sequence**: Project_01_0B_Line (two points define line)
- **Point arrays**: Grids as spatial frameworks
- **Transformations**: Translation, rotation, scaling
- **3D extension**: Adding z-coordinate for spatial position
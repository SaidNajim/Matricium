## Matricium

<div align="center">
  <img src="https://i.ibb.co/41CvbQ1/my-image.png" alt="Matricium Banner" width="150">
</div>

A Command Line Powerful Matrix Computation Tool in Python.

### Objectives
- Design a structure for intuitive matrix input.
- Develop a wide variety of methods to operate on one or more matrices.
- Create a user-friendly interface based on user testing, available across all platforms.

### Usage
- You can either run the .exe file on Windows or run the Python script if you have a Python interpreter installed on any platform.

### Implementation Details
#### Matrix Creation
- **Intuitive Input**: Inspired by a Python Arabic Community video, we implemented a function `create_matrice` that allows users to input matrix details and create matrix objects dynamically.

#### Matrix Operations
- **Access and Manipulation**: Functions iterate over matrix rows and elements to perform operations, storing results in temporary objects.
- **Mathematical Precision**: Operations are based on mathematical formulas provided by Professor M. Abdelali Dreif.

### Key Functions
#### Matrix Input
- `create_matrice()`: Collects matrix name, dimensions, and coefficients from user input, creating a matrix object and adding it to the active matrices database.

#### Matrix Operations
- `somme_matrice(M1)`: Adds two matrices.
- `produit_matrice(M1)`: Multiplies two matrices.
- `scalaire(a)`: Multiplies a matrix by a scalar.
- `trace_matrice()`: Computes the trace of a matrix.
- `inverse()`: Calculates the inverse of a matrix.

### User Interface
The user interface provides easy access to matrix management and operations:
- **Matrix Management**: Create, delete, display, and modify matrices.
- **Matrix Operations**: Sum, subtract, multiply, and test commutativity of matrices. Additional operations include trace, transpose, inverse, and scalar multiplication.

### Contribution
If you find this project helpful, please give it a star on GitHub. Contributions are welcome!

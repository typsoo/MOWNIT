# MOWNIT

Solutions and experiments for the **MOWNIT — Computational Methods in Science and Technology** laboratory course.

The repository contains Jupyter notebooks, Python scripts, visualizations, and supporting data files. The exercises focus on numerical methods, optimization, stochastic algorithms, image processing, and graph analysis.

## Repository Structure

### LAB2 — Solving Systems of Linear Equations

This laboratory focuses on direct methods for solving linear systems and matrix factorization.

- **Gauss–Jordan elimination**  
  Implements the Gauss–Jordan method with partial pivoting for solving systems of linear equations. The implementation is compared with `numpy.linalg.solve` in terms of execution time and numerical accuracy.

- **LU factorization**  
  Performs an in-place LU decomposition of a matrix. The result is verified by reconstructing the original matrix and calculating the error:

  \[
  \|A - LU\|
  \]

### LAB4 — Simulated Annealing

This laboratory applies simulated annealing to several optimization problems.

- **Binary image generation and optimization**  
  Generates binary images with a fixed density of black and white pixels. Simulated annealing is used to organize pixels according to different energy functions and neighborhood definitions.

- **Sudoku solving**  
  Solves Sudoku puzzles using simulated annealing. Candidate solutions are created by filling each \(3 \times 3\) block with valid numbers, while swaps inside blocks are used to reduce conflicts in rows and columns.

- **Travelling Salesman Problem (TSP)**  
  Searches for a short route visiting a collection of cities and returning to the starting point. Simulated annealing is used to improve the route while avoiding local optima. The progress of the optimization is visualized with plots and animations.

### LAB5 — Singular Value Decomposition

This laboratory demonstrates image compression using Singular Value Decomposition (SVD).

The grayscale **Lenna** image is decomposed into singular vectors and singular values. The image is then reconstructed using only the largest singular values. Different ranks are compared to show the trade-off between image quality and the amount of retained data.

### LAB7 — Eigenvalue Algorithms

This laboratory implements iterative methods for finding eigenvalues and eigenvectors.

- **Power method**  
  Finds the dominant eigenvalue and its corresponding eigenvector. The result is compared with the eigenvalues calculated using NumPy.

- **Inverse power method**  
  Finds an eigenvalue close to a selected shift value by repeatedly solving a shifted linear system.

- **Rayleigh quotient iteration**  
  Uses the Rayleigh quotient as a dynamically updated shift to rapidly converge to an eigenvalue of a symmetric matrix. Its performance is compared with the power method.

### LAB8 — PageRank and Random Walks

This laboratory studies ranking algorithms on directed graphs.

- **Basic vertex ranking**  
  Constructs a column-stochastic transition matrix and implements the power method to calculate a PageRank-like ranking of graph vertices.

- The algorithm is tested on several graph structures:
  - Erdős–Rényi random graphs,
  - scale-free graphs,
  - directed cycles with additional chords.

- The results are compared with NumPy's eigenvalue decomposition. The notebooks also visualize graph topology, node rankings, and convergence behavior.


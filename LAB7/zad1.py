import numpy as np
from numpy import linalg as LA
import time
from numpy.random import default_rng

def power_method(A, max_iter=10000, tol=1e-8):
    A = np.asarray(A)
    n = A.shape[0]
    
    x = np.random.rand(n)
    
    for i in range(1, max_iter + 1):
        y = A @ x
        
        norm_inf = np.max(np.abs(y))
        x_new = y / norm_inf
        
        if LA.norm(x - x_new) < tol or LA.norm(x + x_new) < tol:
            x = x_new
            break
            
        x = x_new


    eigenvalue = norm_inf
    
    if np.dot(A @ x, x) < 0:
        eigenvalue = -eigenvalue
        
    eigenvector = x / LA.norm(x)
    
    return eigenvalue, eigenvector, i


if __name__ == "__main__":
    rng = default_rng(45)
    X = rng.standard_normal((500, 500))
    A = (X + X.T) / 2

    start = time.time()
    lam_pm, v_pm, it = power_method(A)
    end_pm = time.time()

    start_numpy = time.time()
    eigvals, eigvecs = LA.eig(A)
    end_numpy = time.time()

    print(f"NumPy Eigenvalues: {np.min(eigvals), np.max(eigvals)}")
    print(f"Power Method Eigenvalue: {lam_pm} (Iterations: {it})")
    print(f"Power Method: {end_pm - start:.6f}s")
    print(f"NumPy eig:    {end_numpy - start_numpy:.6f}s")
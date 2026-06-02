import numpy as np
import scipy.linalg as spla
from numpy import linalg as LA
import time
from numpy.random import default_rng

def inverse_power_method(A, sigma, max_iter=1000, tol=1e-8):
    A = np.asarray(A)
    n = A.shape[0]
    
    I = np.eye(n)
    M = A - sigma * I
    

    lu_piv = spla.lu_factor(M)
    
    x = np.random.rand(n)
    
    for i in range(1, max_iter + 1):
        y = spla.lu_solve(lu_piv, x)
        
        norm_inf = np.max(np.abs(y))
        
        x_new = y / norm_inf
        
        if LA.norm(x - x_new) < tol or LA.norm(x + x_new) < tol:
            x = x_new
            break
            
        x = x_new


    #eigenvalue = np.dot(x, A @ x) / np.dot(x, x)
    eigenvalue = sigma + (1 / norm_inf)
    eigenvector = x / LA.norm(x)
    
    return eigenvalue, eigenvector, i


if __name__ == "__main__":
    rng = default_rng(42)
    X = rng.standard_normal((100, 100))
    A = (X + X.T) / 2  

    true_eigvals = LA.eigvals(A)

    target = np.random.rand() * 10

    start = time.time()
    lam_inv, v_inv, it = inverse_power_method(A, target)
    end = time.time()

    true_eigval = next(
        (val for val in true_eigvals if abs(val - lam_inv) < 1e-3),
        None 
    )

    print(f"Target sigma: {target:.4f}")
    print(f"Found Eigenvalue: {lam_inv:.8f} (True was: {true_eigval})")
    print(f"Iterations: {it}")
    print(f"Time: {end - start:.6f}s")
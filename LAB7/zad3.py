import numpy as np
import scipy.linalg as spla
from numpy import linalg as LA
import time
from numpy.random import default_rng
from zad1 import power_method

def rayleigh_quotient_iteration(A, max_iter=1000, tol=1e-8):
    A = np.asarray(A)
    n = A.shape[0]
    I = np.eye(n)
    
    x = np.random.rand(n)
    x = x / LA.norm(x)
    
    for i in range(1, max_iter + 1):
        sigma = np.dot(x, A @ x) / np.dot(x, x)
        
        M = A - sigma * I
        

        lu_piv = spla.lu_factor(M)
        y = spla.lu_solve(lu_piv, x)
   
            
        x_new = y / LA.norm(y)
        
        if LA.norm(x - x_new) < tol or LA.norm(x + x_new) < tol:
            x = x_new
            break
            
        x = x_new

    eigenvalue = np.dot(x, A @ x) / np.dot(x, x)
    
    return eigenvalue, x, i



if __name__ == "__main__":

    rng = default_rng(10)
    X = rng.standard_normal((500, 500))
    A = (X + X.T) / 2 

    start_pm = time.time()
    lam_pm, v_pm, iter_pm = power_method(A)
    end_pm = time.time()

    print("\n1. Metoda Potęgowa (Szuka dominującej wartości):")
    print(f"   Znaleziona wartość: {lam_pm:.8f}")
    print(f"   Liczba iteracji:    {iter_pm}")
    print(f"   Czas wykonania:     {end_pm - start_pm:.6f}s")

    start_rqi = time.time()
    lam_rqi, v_rqi, iter_rqi = rayleigh_quotient_iteration(A)
    end_rqi = time.time()

    print("\n2. Iteracje z Ilorazem Rayleigha (RQI):")
    print(f"   Znaleziona wartość: {lam_rqi:.8f} (Znajduje losową najbliższą)")
    print(f"   Liczba iteracji:    {iter_rqi}")
    print(f"   Czas wykonania:     {end_rqi - start_rqi:.6f}s")
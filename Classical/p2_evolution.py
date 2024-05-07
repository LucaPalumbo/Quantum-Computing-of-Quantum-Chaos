import numpy as np
import matplotlib.pyplot as plt
from chirikov_map import chirikov_map

if __name__ == '__main__':
    T = 1
    N = 400
    n = 5000


    for k in [4,6,8,10,12]:
        ps2 = np.array( [0]*(N+1), dtype=float )
        for i in range(n):
            theta0 = np.random.rand()*2*np.pi
            p0 = np.random.rand()*2*np.pi - np.pi
            thetas, ps = chirikov_map(theta0=theta0, p0=p0, k=k, T=T, N=N)
            ps2 += np.array(ps)**2 
        ps2 /= n
        kicks = np.linspace(0, N+1, N+1)
        plt.plot(kicks, ps2, label=f'K = {k}')


    plt.xlabel("kicks")
    plt.ylabel("<p^2>")
    plt.legend()
    #plt.show()
    plt.savefig("p2_evolution.png")

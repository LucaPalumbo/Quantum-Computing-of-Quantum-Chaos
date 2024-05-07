import numpy as np
import matplotlib.pyplot as plt

from chirikov_map import chirikov_map



if __name__ == "__main__":
    k = 0.9716
    k = 4
    T = 1
    N = 1000

    for i in range(500):
        theta0 = np.random.rand()*2*np.pi
        p0 = np.random.rand()*2*np.pi - np.pi
        thetas, ps = chirikov_map(theta0=theta0, p0=p0, k=k, T=T, N=N)
        plt.errorbar(thetas, ps, fmt='o', markersize=1, alpha=0.1)

    plt.xlabel("theta")
    plt.ylabel("p")
    plt.ylim(-np.pi, np.pi)
    plt.title(f"Kicked Rotator, K = {k}")
    #plt.show()
    plt.savefig("kicked_rotator3.png")
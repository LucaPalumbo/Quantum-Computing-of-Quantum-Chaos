import numpy as np
import matplotlib.pyplot as plt


def chirikov_map(theta0, p0, k, T, N):
    theta_list = [theta0]
    p_list = [p0]
    p = p0
    theta = theta0
    for i in range(N):
        p = ( p + k * np.sin(theta) ) % (2*np.pi)
        theta = ( theta + T*p ) % (2*np.pi)
        theta_list.append(theta)
        p_list.append(p)
    for i in range(N+1):
        if p_list[i] >= np.pi:
            p_list[i] -= 2*np.pi
    return theta_list, p_list



if __name__ == "__main__":
    k = 0.9716
    T = 1
    N = 1000

    datas = map(lambda x: chirikov_map(theta0=x, p0=-np.pi/2, k=k, T=T, N=N), np.linspace(0, 2*np.pi, 50))
    datas1 = map(lambda x: chirikov_map(theta0=x, p0=0, k=k, T=T, N=N), np.linspace(0, 2*np.pi, 50))
    datas2 = map(lambda x: chirikov_map(theta0=x, p0=np.pi/2, k=k, T=T, N=N), np.linspace(0, 2*np.pi, 50))


    for data in datas:
        plt.scatter(data[0], data[1], marker='.')
    for data in datas1:
        plt.scatter(data[0], data[1], marker='.')
    for data in datas2:
        plt.scatter(data[0], data[1], marker='.')

    plt.xlabel("theta")
    plt.ylabel("p")
    plt.title("Kicked Rotator")
    #plt.show()
    plt.savefig("kicked_rotator.png")
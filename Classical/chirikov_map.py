import numpy as np 
def chirikov_map(theta0, p0, k, T, N):
    theta_list = [theta0]
    p_list = [p0]
    p = p0
    theta = theta0
    for i in range(N):
        p     = ( p + k * np.sin(theta) ) 
        theta = ( theta + T*p )            % (2*np.pi)
        theta_list.append(theta)
        p_list.append(p)
    #for i in range(N+1):
    #    if p_list[i] >= np.pi:
    #        p_list[i] -= 2*np.pi
    return theta_list, p_list

def rhs_SDZR(t,c, K):

    S, E, Z, R = c
    beta, sigma, a, N ,_= K
    SZ = S*Z/N

    d_S = -(beta*SZ)
    d_E = beta*SZ-sigma*E
    d_Z = sigma*E-a*SZ
    d_R = a*SZ


    return np.array([d_S,d_E,d_Z,d_R])
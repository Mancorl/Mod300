def beta_f(t,beta,landa):

    """
    Zombie attack function
    Input
    -----
    t: float, time
    beta: float, array of Konstant beta0
    landa: float, array of Konstant : landa
    Output
    ------
    c : array, fusjen of beta_f(t)
    """

    return beta*np.exp(-1*landa*t)

def rhs_SDZR_EBOLA(t,c, K):

    """
    Zombie attack function
    Input
    -----
    t: float, time
    c: float, array of S, E, Z, R
    K: float, array of Konstant : beta, sigma, gamma, N
    Output
    ------
    c : array, array of d_S,d_E,d_Z,d_R
    """


    S, E, Z, R = c
    beta_0,sigma, gamma, N ,landa= K
    beta = beta_f(t,beta_0,landa)
    SZ = S*Z/N

    d_S = -(beta*SZ)
    d_E = beta*SZ-sigma*E
    d_Z = sigma*E-gamma*Z
    d_R = gamma*Z


    return np.array([d_S,d_E,d_Z,d_R])
def omega(t, a, attacks):
    """
    Zombie attack function
    Input
    -----
    t: float, time
    a: float, strength of attacks
    attacks: a list with times for attacks
    Output
    ------
    sys[0]: float
    """
    return a*np.sum([np.exp(-.5*(t-ti)**2) for ti in attacks])

def rhs_SDZR_attacks(t,c, K,attacks):

    """
    Zombie attack function
    Input
    -----
    t: float, time
    c: float, array of S, E, Z, R
    K: float, array of Konstant : beta, sigma, alfa, N, a
    attacks: a list with times for attacks
    Output
    ------
    c : array, array of d_S,d_E,d_Z,d_R
    """


    S, E, Z, R = c
    beta, sigma, alfa, N, a = K
    w_t = omega(t, a, attacks)

    SZ = S*Z/N

    d_S = -(beta*SZ)
    d_E = beta*SZ-sigma*E
    d_Z = sigma*E-(alfa+w_t)*SZ
    d_R = (alfa+w_t)*SZ


    return np.array([d_S,d_E,d_Z,d_R])
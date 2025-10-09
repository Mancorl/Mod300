def ode_solver_adaptiv(t0, t_final, c0, eps, f, method, *args, **kwargs):
    """
    A simple ODE solver

    Input
    -----
    t0: float, starting time
    t_final: float, end time
    c0: float, initial condition
    eps: float, accuracy
    f: ode function (rhs) f(t,c,tau)
    tau: float, a parameter

    Output
    -----
    t, c
    """
    c = []
    t = []
    c.append(c0) # initial conditions
    t.append(t0)
    dt_old = 1e-2
    if method == 'Euler':
        p = 1
    elif method == 'RK2':
        p = 2
    elif method == 'RK4':
        p = 4
    else:
        assert ValueError('Method not implemented')
    while t[-1] < t_final:
        c_old = c[-1]
        eps_calc = 10*eps #just to enter while loop
        while eps_calc > eps:
            dt = dt_old
            c_long = c_old + step(t[-1], c_old, dt, f, method, *args, **kwargs)
            c_half = c_old + step(t[-1], c_old, 0.5*dt, f, method, *args, **kwargs)
            c_two_half = c_half + step(t[-1]+0.5*dt, c_half, 0.5*dt, f, method, *args, **kwargs)
            eps_calc = np.linalg.norm((c_long-c_two_half)/(2**p-1))
            eps_calc = np.ceil(eps_calc * 1e5) / 1e5
            dt_old = dt*(eps/eps_calc)**(1/(p+1))
            if dt_old + t[-1] >= t_final:
                dt = t_final - t[-1]
                c_two_half = c_old + step(t[-1], c_old, dt, f, method, *args, **kwargs)
                break
        c.append(c_two_half)
        t.append(t[-1]+dt)
    return np.array(t), np.array(c)


def step(t, c_old, dt, f, method, *args, **kwargs):
    """
    Awesome doc string
    """
    if method == 'Euler':
        return dt*f(t, c_old, *args, **kwargs)
    elif method == 'RK2':
        k1 = np.array(dt*f(t, c_old, *args, **kwargs))
        return dt*f(t+dt*0.5, c_old + 0.5*k1, *args, **kwargs)
    elif method == 'RK4':
        k1 = np.array(f(t, c_old, *args, **kwargs))
        k2 = np.array(f(t + dt * 0.5, c_old + 0.5 * dt * k1, *args, **kwargs))
        k3 = np.array(f(t + dt * 0.5, c_old + 0.5 * dt * k2, *args, **kwargs))
        k4 = np.array(f(t + dt, c_old + dt * k3, *args, **kwargs))
        return (dt / 6.0) * (k1 + 2*k2 + 2*k3 + k4)
    else:
        raise ValueError('Method ot implemented')
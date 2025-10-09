
Z0 = 1
S0 = N - Z0
E0 = 0
R0 = beta/(alfa +w_t)
c0= np.array([S0,E0,Z0,R0])
gamma = 1/7
sigma = 1/9.7
N = 10e7
t_final = 700
eps = 0.001
T_probabilety = 50
porsent = 60
#landa = -1*np.log(porsent/100)/T_probabilety
landa = 0.002 # 0.002
beta = 0.255 # 0.25


file_path = "ebola_cases_guinea.dat"
x_f,_,y_f = read_file(file_path)
t,Z = ode_solver_adaptiv(0, t_final, c0, eps,  rhs_SDZR_EBOLA,'RK4', np.array([beta,sigma,gamma,N,landa]))

plt.plot(t,Z[:,2],'-*', label="modelering")
plt.plot(x_f,y_f,'*', label="fusjon")

plt.legend()
plt.grid()
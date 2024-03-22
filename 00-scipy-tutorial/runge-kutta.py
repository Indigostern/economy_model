from scipy.integrate import RK45
import numpy as np
import pylab          # plotting of results

def f(t, y):
    """this is the rhs of the ODE to integrate, i.e. dy/dt=f(y,t)"""
    return -2 * y * t

y0 = [1]           # initial value y0=y(t0)
t0 = 0             # integration limits for t: start at t0=0
tf = 2             # and finish at tf=2
ts = np.linspace(t0, tf, 100)  # 100 points between t0 and tf

# sol = solve_ivp(fun=f, t_span=[t0, tf], y0=y0)  # computation of SOLution 
# sol = solve_ivp(fun=f, t_span=[t0, tf], y0=y0, atol=1e-8, rtol=1e-8)
# sol = solve_ivp(fun=f, t_span=[t0, tf], y0=y0, t_eval=ts) 
sol = RK45(fun=f, t0=t0, y0=y0, t_bound=tf, first_step=.02, atol=1e-8, rtol=1e-8)

t_values = []
y_values = []
for i in range(100):
    # get solution step state
    sol.step()
    t_values.append(sol.t)
    y_values.append(sol.y[0])
    # break loop after modeling is finished
    if sol.status == 'finished':
        break


# pylab.plot(sol.t, sol.y[0], '.')
pylab.plot(t_values, y_values, '.')
pylab.xlabel('t'); pylab.ylabel('y(t)')
pylab.show()
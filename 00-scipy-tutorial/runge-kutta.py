from scipy.integrate import solve_ivp
import numpy as np
import matplotlib  
matplotlib.use('Qt5Agg')
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
sol = solve_ivp(fun=f, t_span=[t0, tf], y0=y0, t_eval=ts) 

pylab.plot(sol.t, sol.y[0], '.')
pylab.xlabel('t'); pylab.ylabel('y(t)')
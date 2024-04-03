from scipy.integrate import RK45
import numpy as np
import matplotlib.pyplot as plt

def f(t, y):
    """this is the rhs of the ODE to integrate, i.e. dy/dt=f(y,t)"""
    return [y[0] - y[1], y[1] - y[0]]

y0 = [1, 0]           # initial value y0=y(t0)
t0 = 0             # integration limits for t: start at t0=0
tf = 2     

sol = RK45(fun=f, t0=t0, y0=y0, t_bound=tf, first_step=.02, max_step=.1, atol=1e-6, rtol=1e-6)

t_values = []
y0_values = []
y1_values = []
for i in range(100):
    # get solution step state
    sol.step()
    t_values.append(sol.t)
    y0_values.append(sol.y[0])
    y1_values.append(sol.y[1])
    # break loop after modeling is finished
    if sol.status == 'finished':
        break

fig, axs = plt.subplots(2)
fig.suptitle('Vertically stacked subplots')
axs[0].plot(t_values, y0_values,'.')
axs[1].plot(t_values, y1_values,'.')
plt.xlabel('t')
plt.show()
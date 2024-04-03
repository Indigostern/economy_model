from scipy.integrate import RK45
import numpy as np
import matplotlib.pyplot as plt
import math

# Vars
alpha = 0.2
productivity = 1
consumption = 0.5
price = 1
dprice = 0
interest_d = 1.08
interest_a = 1.06

def logistical(t, k, t0):
    return 1/(1+math.exp(-k*(t-t0)))

def f(t, y):
    """this is the rhs of the ODE to integrate, i.e. dy/dt=f(y,t)"""
    return [
        1/(1-alpha)*(productivity - consumption + y[0]*(interest_a - dprice/price) - y[1]/price*interest_d)*logistical(y[0], 1e2, 0), 
        (2*y[1]*interest_d - y[0] * (price*interest_a - dprice) - price*(productivity - consumption))*logistical(y[1], 1e2, 0)
        ]

y0 = [1, 1]           # initial value y0=y(t0)
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

plt.close('all')
fig, (ax1, ax2) = plt.subplots(2)
fig.suptitle('Vertically stacked subplots')
ax1.plot(t_values, y0_values,'.')
ax2.plot(t_values, y1_values,'.')
plt.xlabel('t')
ax1.set(ylabel='assets')
ax2.set(ylabel='debt')
plt.show()
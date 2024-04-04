from scipy.integrate import RK45
import matplotlib.pyplot as plt
import math

# Vars
productivity = 2.5
consumption = 0.5
price = 1
dprice = 0
interest_a = 0.08
interest_d = 0.1

def logistical(t, k, t0):
    return 1/(1+math.exp(-k*(t-t0)))

def Rc(t):
    if(t > 1 and t < 1.5):
        return 16
    else:
        return 0

def f(t, y):
    """this is the rhs of the ODE to integrate, i.e. dy/dt=f(y,t)"""
    assets = y[0]
    debt = y[1]
    theta = assets * price * interest_a - debt * interest_d
    En = price * (productivity - consumption) + theta
    GammaR = 2 * logistical(debt, 1e1, 0) - 1
    Rr = max(0., En * GammaR)
    return [
        1 / price * (En + Rc(t) - Rr - assets * dprice), 
        debt * interest_d + Rc(t) - Rr
        ]

assets0, debt0 = 0, 0
y0 = [assets0, debt0]           # initial value y0=y(t0)
t0 = 0             # integration limits for t: start at t0=0
tf = 10     

sol = RK45(fun=f, t0=t0, y0=y0, t_bound=tf, first_step=.02, max_step=.1, atol=1e-6, rtol=1e-6)

t_values = []
y0_values = []
y1_values = []
Rc_values = []
while True:
    # get solution step state
    sol.step()
    t_values.append(sol.t)
    y0_values.append(sol.y[0])
    y1_values.append(sol.y[1])
    Rc_values.append(Rc(sol.t))
    # break loop after modeling is finished
    if sol.status == 'finished':
        break

fig, axs = plt.subplots(3)
fig.suptitle('Vertically stacked subplots')
axs[0].plot(t_values, y0_values,'.')
axs[1].plot(t_values, y1_values,'.')
axs[2].plot(t_values, Rc_values)
plt.xlabel('t')
axs[0].set(ylabel='assets')
axs[1].set(ylabel='debt')
axs[2].set(ylabel="Rc perturbation")
plt.show()
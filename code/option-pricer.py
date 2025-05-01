import numpy as np
import matplotlib.pyplot as plt

stock_init = 100
volatility = 0.015
r = 0.06

runs = 10
scale = 252

x = np.linspace(0, 1000, 1000)
A = np.zeros(1000)
s_t = stock_init
d_t = 1/scale
mu = r # usually drift is the interest rate
K = 112

put_list, call_list, chooser_list = [0] * runs, [0] * runs, [0] * runs

for j in range(runs):
    for i in range(1000):
        dW_t = np.random.normal(loc=0, scale=np.sqrt(d_t))
        dS_t = mu * s_t * d_t + volatility * s_t * dW_t
        s_t += dS_t
        A[i] = s_t

    avg = np.sum(A) / 1000
    put = max(0,K - avg)
    call = max(0,avg - K)
    dT = np.exp(-r * (1000 / scale))
    chooser = max(put, call)
    put_list[j] = put * dT
    call_list[j] = call * dT
    chooser_list[j] = chooser * dT
    s_t = stock_init
    print(avg)

    plt.plot(x, A)

print(put_list)
print(call_list)
print(chooser_list)
plt.savefig('../figs/black-scholes-fan.png')
print(f"put: {np.average(put_list)}. call: {np.average(call_list)}, chooser: {np.average(chooser_list)}")
    
    
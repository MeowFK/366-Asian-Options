import numpy as np
import matplotlib.pyplot as plt
import tqdm

np.random.seed(21367)

S0 = 100
sigma = 0.3
r = 0.06
mu = r
K = 100
T = 180 / 365
intervals = 10000

x = np.linspace(0, T, intervals+1)
x2 = np.linspace(0, T, intervals)
d_t = T/intervals

A1 = [S0]
avgs = [K]
for i in tqdm.trange(0, x.size - 1):
    dW_t = np.random.standard_normal() * np.sqrt(d_t)
    dS_t = A1[-1] * mu * d_t + A1[-1] * sigma * dW_t
    A1.append(A1[-1] + dS_t)
    avgs.append(np.sum(A1[0:i])/i)

puts = [max(0,K - avgs[i+1]) for i in tqdm.trange(0, x.size - 1)]
calls = [max(0,avgs[i+1] - K) for i in tqdm.trange(0, x.size - 1)]

plt.plot(x, A1, label="Stock Price")
plt.plot(x, avgs, label="Average Price")
plt.xlabel("Time (in years)")
plt.ylabel("Value (in dollars)")
plt.title("Stock value and its average over 6 months using Black-Scholes Model")
plt.legend()
plt.savefig('../figs/blackscholes-stock-T:180')
plt.close()

plt.plot(x2, puts, label="Put Option Value")
plt.plot(x2, calls, label="Call Option Value")
plt.xlabel("Time (in years)")
plt.ylabel("Value (in dollars)")
plt.title("Asian option value over 6 months using Black-Scholes Model")
plt.legend()
plt.savefig('../figs/blackscholes-option-payout-T:180')


    
    
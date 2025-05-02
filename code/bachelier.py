import numpy as np
import matplotlib.pyplot as plt
import tqdm

np.random.seed(21366)

S0 = 100
vol = 30.0
T = 180 / 365
intervals = 10000
d_t = T/intervals
strike = 100

x = np.linspace(0, T, intervals+1)
x2 = np.linspace(0, T, intervals)
y = [S0]
avgs = [strike]
for i in tqdm.trange(0, x.size-1):
  dSt = vol * ( np.sqrt(d_t) * np.random.standard_normal() )
  y.append(y[-1] + dSt)
  avgs.append(np.sum(y[0:i])/i)
  
puts = [max(0,strike - avgs[i]) for i in tqdm.trange(0, x.size - 1)]
calls = [max(0,avgs[i] - strike) for i in tqdm.trange(0, x.size - 1)]

plt.plot(x, y, label="Stock Price")
plt.plot(x, avgs, label="Average Price")
plt.xlabel("Time (in years)")
plt.ylabel("Value (in dollars)")
plt.title("Stock value and its average over 6 months using Bachelier Model")
plt.legend()
plt.savefig('../figs/bachelier-stock-T:180')
plt.close()

plt.plot(x2, puts, label="Put Option Value")
plt.plot(x2, calls, label="Call Option Value")
plt.xlabel("Time (in years)")
plt.ylabel("Value (in dollars)")
plt.title("Asian option value over 6 months using Bachelier Model")
plt.legend()
plt.savefig('../figs/bachelier-option-payout-T:180')
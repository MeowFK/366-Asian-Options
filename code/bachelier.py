import numpy as np
import matplotlib.pyplot as plt
import tqdm

# np.random.seed(101)

S0 = 100
vol = 0.8
T = 1000
intervals = 10000
strike = 110

x = np.linspace(0, T, intervals+1)
y = [S0]
for i in tqdm.trange(0, x.size-1):
  dSt = vol * ( np.sqrt( T / intervals ) * np.random.standard_normal() )
  y.append(y[-1] + dSt)

plt.plot(x, y, label="Stock Price")

rolling_sum = np.cumsum(y)
rolling_avg = rolling_sum / np.arange(1, len(y)+1)
# plt.plot(x, rolling_avg, label="Asian Payout")
plt.title(f"Bachelier vol:{vol}")
plt.legend()
plt.savefig(f'../figs/bachelier-vol:{vol}-T:1000.png')
plt.close()

# put = np.maximum(strike - rolling_avg, 0)
# call = np.maximum(rolling_avg - strike, 0)
# chooser = np.maximum(put, call)

# plt.plot(x, put, label="Put payout")
# plt.plot(x, call, label="Call payout")
# plt.plot(x, chooser, label="Chooser payout", alpha=0.5)

# plt.title("Asian Chooser Payout over Time 1000")
# plt.legend()
# plt.savefig('../figs/bachelier-asian-chooser-T:1000')
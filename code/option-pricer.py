import numpy as np
import matplotlib.pyplot as plt
import tqdm

# No seed so that each call to np.random is actually random

S0 = 100
sigma = 0.1
sigma_abs = sigma * S0
r = 0.005
mu = r
K = 100
num_days = 180
T = num_days / 365
intervals = 10000
num_trials = 1000

x = np.linspace(0, T, intervals+1)
d_t = T/intervals

# Discount Factor
dT = np.exp(-r * T)

put_list1, call_list1, chooser_list1 = [0] * num_trials, [0] * num_trials, [0] * num_trials
put_list2, call_list2, chooser_list2 = [0] * num_trials, [0] * num_trials, [0] * num_trials

for j in range(num_trials):
    y = [S0]
    A1 = [S0]
    for i in tqdm.trange(0, x.size - 1):
        # Black-Scholes Model
        dW_t = np.random.standard_normal() * np.sqrt(d_t)
        dS_t = A1[-1] * mu * d_t + A1[-1] * sigma * dW_t
        A1.append(A1[-1] + dS_t)
        
        # Bachelier Model
        dSt = sigma_abs * (np.sqrt(d_t) * np.random.standard_normal())
        y.append(y[-1] + dSt)
    
    # Black-Scholes Model
    avg1 = np.sum(A1) / len(A1)
    put = max(0,K - avg1)
    call = max(0,avg1 - K)
    chooser = max(put, call)
    put_list1[j] = put * dT
    call_list1[j] = call * dT
    chooser_list1[j] = chooser * dT
    
    # Bachelier Model
    avg2 = np.sum(y) / len(y)
    put = np.maximum(K - avg2, 0)
    call = np.maximum(avg2 - K, 0)
    chooser = np.maximum(put, call)
    put_list2[j] = put * dT
    call_list2[j] = call * dT
    chooser_list2[j] = chooser * dT

print(f"Black-Scholes Model - put: {np.average(put_list1)}. call: {np.average(call_list1)}, chooser: {np.average(chooser_list1)}")
print(f"Bachelier Model - put: {np.average(put_list2)}. call: {np.average(call_list2)}, chooser: {np.average(chooser_list2)}")
    
    
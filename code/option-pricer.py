import numpy as np
import matplotlib.pyplot as plt
import tqdm

S0 = 100
sigma = 0.3
r = 0.06
mu = 0.1
K = 70
T = 1000
intervals = 10000

x1 = np.linspace(0, T, intervals+1)
A1 = np.zeros(intervals)
s_t = S0
d1_t = 1/365

x2 = np.linspace(0, T, intervals+1)
y = [S0]  



put_list1, call_list1, chooser_list1 = [0] * 3000, [0] * 3000, [0] * 3000
put_list2, call_list2, chooser_list2 = [0] * 3000, [0] * 3000, [0] * 3000


for j in range(1000):
    for i in tqdm.trange(0, x1.size - 1):
        # Black-Scholes Model
        dW_t = np.random.normal(loc=0, scale=(i/365))
        dS_t = mu * d1_t + sigma * dW_t * np.sqrt(d1_t)
        s_t += s_t * dS_t
        A1[i] = s_t
        
        # Bachelier Model
        dSt = sigma * ( np.sqrt( T / intervals ) * np.random.standard_normal() )
        y.append(y[-1] + dSt)

    # Discount Factor
    dT = np.exp(-r * (T/365))
    
    # Black-Scholes Model
    avg1 = np.sum(A1) / len(A1)
    put = max(0,K - avg1)
    call = max(0,avg1 - K)
    chooser = max(put, call)
    put_list1[j] = put * dT
    call_list1[j] = call * dT
    chooser_list1[j] = chooser * dT
    s_t = S0
    
    # Bachelier Model
    avg2 = y[len(y)-1] / len(y)
    put = np.maximum(K - avg2, 0)
    call = np.maximum(avg2 - K, 0)
    chooser = np.maximum(put, call)
    put_list2[j] = put * dT
    call_list2[j] = call * dT
    chooser_list2[j] = chooser * dT

print(f"Black-Scholes Model - put: {np.average(put_list1)}. call: {np.average(call_list1)}, chooser: {np.average(chooser_list1)}")
print(f"Bachelier Model - put: {np.average(put_list2)}. call: {np.average(call_list2)}, chooser: {np.average(chooser_list2)}")
    
    
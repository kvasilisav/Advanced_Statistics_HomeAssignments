import numpy as np
import scipy

# df2 = pd.read_csv('/content/part 2. input.csv')
# df2 = df2[df2.columns[0]].rename('gamma')
# S = df2.mean()
# L = np.log(df2).mean()

S = 4.514982304515785
L = 1.4544518507143103
def func(x, S, L):
  k = x[0]
  t = x[1]
  return S/t - k*L + scipy.special.loggamma(k) + k*np.log(t)
result = scipy.optimize.minimize(func, x0 = [9, 0.5], args = (S, L), method = 'SLSQP')
with open('output.txt', 'w') as f:
    print(*result.x, file=f) 

# def func_approx(x, S, L):
#   k = x[0]
#   t = x[1]
#   return S/t - k*L + (k-1)*np.log(k) - k + np.log(k-1)/2 + k*np.log(t)
# result_approx = scipy.optimize.minimize(func_approx, x0 = [9, 0.5], args = (S, L), method = 'SLSQP')
# with open('output.txt', 'w') as f:
#     print(*result_approx.x, file=f)   


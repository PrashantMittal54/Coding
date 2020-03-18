#OLS estimation of AR(1):
#Consider the following AR(1) model:
# xt = a + p*xt−1 + et
#Generate data from this model. Then estimate the model using ordinary least squares. The estimated ˆp that
#you will find will be biased. Write a simulation to study this bias. See if you can find the functional form of
#the bias via simulation.
1

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from cleands import least_squares_regressor
import statsmodels.formula.api as smf


# simulating AR(1) model
np.random.seed(1010)
sample = [10, 25, 50, 75, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600]
rho_list = [0.95, 0.90, 0.80, 0.70, 0.60, 0.50, 0.40, 0.20, 0.10, -0.1, -0.2, -0.3, -0.4, -0.5, -0.6]

dataf = pd.DataFrame()
ax = plt.subplot(111)
for rho in rho_list:
    bias_list = []
    for n in sample:
        x = np.random.normal(size=(n, 1))
        y = np.zeros(shape=(n,))
        for t in range(1,n):
            y[t] = rho*y[t-1]+x[t]
        ones = np.ones(shape=(n-1,1))
        x = y[:-1].reshape(-1,1)
        y = y[1:]
        x = np.hstack((ones, x))
        model = least_squares_regressor(x, y)
        print(model.r_squared)
        bias = rho - model.params[1]
        bias_list.append(bias)
        dataf = dataf.append({"Bias": bias, "Size_Inv": 1 / n, "Rho": rho}, ignore_index=True)
    ax.plot(sample, bias_list, label= 'rho = {}'.format(rho))
plt.title('Bias Vs Sample Size')
plt.xlabel('Sample Size')
plt.ylabel('Bias')
ax.legend(loc='upper center', bbox_to_anchor=(0.5, 1.00), shadow=True, ncol=2)
plt.show()

# find optimum values of parameters or their functional form:
model2 = smf.ols(formula='Bias ~ Rho + Size_Inv + Size_Inv:Rho', data=dataf).fit()
print(model2.summary().tables[1])
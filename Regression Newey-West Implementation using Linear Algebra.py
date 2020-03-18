#Extend the linear model code to implement a Newey-West corrected OLS estimator with
#autocovariance term. The robust variance covariance matrix for this Newey-West estimator is
#Vˆar(ˆ) = (X0X)−1X0ˆX(X0X)−1

import numpy as np
import pandas as pd

class linear_model:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.b = np.linalg.solve(x.T@x,x.T@y)
        e = y-x@self.b
        self.vb = self.vcov_b(e)
        self.se = np.sqrt(np.diagonal(self.vb))
        self.tstat = self.b/self.se

    def vcov_b(self,e):
        x = self.x
        return e.var()*np.linalg.inv(x.T@x)


class white(linear_model):
    def __init__(self, x, y):
        linear_model.__init__(self, x, y)

    def vcov_b(self,e):
        x = self.x
        meat = np.diagflat(e**2)
        bread = np.linalg.inv(x.T@x)@x.T
        sandwich = bread@meat@bread.T
        return sandwich


class nw_hac(linear_model):
    def __init__(self, x, y):
        linear_model.__init__(self, x, y)

    def vcov_b(self,e):
        x = self.x[1:]
        n = e.shape[0]
        e_t_1 = np.zeros(n).reshape(-1, 1)
        for t in range(1, n):
            e_t_1[t] = e[t - 1]
        e = e[1:]
        e_t_1 = e_t_1[1:]
        sigma1 = np.cov(e.flatten(), e_t_1.flatten())[0, 1]
        #creating Omega matrix as a meat
        meat = (np.diagflat(np.full([1, n-2],sigma1),-1))+(np.diagflat(e**2))+(np.diagflat(np.full([1, n-2],sigma1),1))
        bread = np.linalg.inv(x.T@x)@x.T
        sandwich = bread@meat@bread.T
        return sandwich

#data preparation for testing Newey-West
n = 1000
np.random.seed(100)
x = np.random.normal(size=(n,1))
e = np.random.normal(size=(n,1))
for t in range(1,n):
    x[t]+= 0.75*x[t-1]
    e[t]+= 0.75*e[t-1]
y = e

model1 = nw_hac(x, y)
print('Value of Standard Error is {0}'.format(model1.se))
print('Value of T-Statistics is {0}'.format(model1.tstat))

# output verification from standard python package.
import statsmodels.formula.api as smf

df = pd.DataFrame({'a':x.flatten(), 'b':y.flatten()})
reg = smf.ols('a ~ b',data=df).fit(cov_type='HAC',cov_kwds={'maxlags':1})
print(reg.summary())

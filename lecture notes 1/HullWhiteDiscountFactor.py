import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


class HullWhiteDiscountFactorCurve():
    def __init__(self, r, kappa, theta, vol):
        self.r = r
        self.kappa = kappa
        self.theta = theta
        self.vol = vol

        self.kappa2 = kappa * kappa
        self.four_kappa = 4.0 * kappa

        self.variance = vol * vol
        self.variance_over_2 = self.variance / 2.0

    def get_df(self, t):
        B = np.array((1.0 - np.exp(-self.kappa * t)) / self.kappa)
        #print(B)
        A = np.exp(((B - t) * (self.kappa2 * self.theta - self.variance_over_2)) / self.kappa2
                   - (self.variance * B * B / self.four_kappa))

        return A * np.exp(-self.r * B)

if __name__ == '__main__':
    curve = HullWhiteDiscountFactorCurve(0.05, 0.10, 0.05, .01)
    t = np.linspace(0.25, 10, 40)
    dfs = curve.get_df(t)
    df = pd.DataFrame(dfs, index=t)
    print(df)
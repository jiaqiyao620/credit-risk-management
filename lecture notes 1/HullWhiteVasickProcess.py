import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from math import sqrt

class HullWhiteVasicekProcess():

    def __init__(self, r0, kappa, theta, vol):
        self.r0 = r0
        self.kappa = kappa
        self.theta = theta
        self.vol = vol

        self.kappa2 = kappa * kappa
        self.four_kappa = 4.0 * kappa

        self.variance = vol * vol
        self.variance_over_2 = self.variance / 2.0

    def generate_path(self, numberOfTimeSteps, time_step_size_in_years):

        path = []
        current = self.r0
        dt = time_step_size_in_years
        vol_sqrt_dt = self.vol * sqrt(dt)
        for i in range(numberOfTimeSteps):
            path.append(current)
            drift = self.kappa * (self.theta - current) * dt
            shock = vol_sqrt_dt * np.random.normal(0,1)
            current += (drift + shock)

        t = np.linspace(0, numberOfTimeSteps * time_step_size_in_years, numberOfTimeSteps)
        return pd.DataFrame(path, index=t)

if __name__ == '__main__':
    process = HullWhiteVasicekProcess(0.05, 0.10, 0.05, .01)
    path = process.generate_path(40, .25)
    print(path)


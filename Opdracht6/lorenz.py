import random
from scipy.integrate import odeint
from numpy import arange


class Lorenz:
    def __init__(self, Y, sigma=10, rho=28, betha=8/3):
        self.Y = Y
        self.sigma = sigma
        self.rho = rho
        self.betha = betha
    
    def _solve_(self, T, dt):
        return self.solve(T, dt)
        
    def lorenzFunc(self, X, t):
        [x, y, z] = X
        return [self.sigma*(y - x), x * (self.rho -z) -y, x*y -self.betha*z]
        
    def solve(self,T,dt):
        y0 = self.Y
        tijd = arange(0, T, dt)
        y=odeint(self.lorenzFunc, y0, tijd)
        return y
    
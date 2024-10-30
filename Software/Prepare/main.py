import numpy as np
import scipy.integrate as sp_int
import scipy
import tqdm 
import matplotlib.pyplot as plt

### Вектор в системе - [x,y,z]
class Fluid:
    H = np.zeros((3))
    V = np.zeros((3))
    rho = 1000
    p = 1
    def __init__(self) -> None:
        pass
    def SetSize(self, sizeX, sizeY, sizeZ):
        np.resize(self.H, (sizeX, sizeY, sizeZ))
        np.resize(self.V, (sizeX, sizeY, sizeZ))
    def SetRho(self, new_rho):
        self.rho = new_rho
    def SetP(self, new_p):
        self.p = new_p
    def div(vecSpace):
        return scipy.stats.power_divergence(vecSpace, axis = None)
    def equalition1(self, dt):
        pass
        #self.p += -
import numpy as np
import scipy.integrate
from tqdm import tqdm
from math import sin

def KuramotoOmega(phi, t, omega,  K):
    dphi_dt = omega + np.sin(phi) * (K @ np.cos(phi)) - np.cos(phi) * (K @ np.sin(phi))
    return dphi_dt

def ENERGY_TEMP(T, t, a, b, c, P):
    dW_dT = P/a + (b/a)*T*T - np.sqrt(T) * c/a - T/t  
    return dW_dT
def Integrator(resolution, duration, T_0, a,b,c,P):
    Time = np.linspace(0,duration, int(duration/resolution))
    Temp = scipy.integrate.odeint(ENERGY_TEMP, T_0, Time, args=(a,b,c,P))
    #dT_dt = np.array([ENERGY_TEMP(phi_t, 0, omegas, K) for phi_t in Phi_t])
    return Time, Temp#, dT_dt.T

def Integrator_stpd(resolution, duration, T_0, a,b,c,P):
    Time = np.linspace(0,duration, int(duration/resolution))
    T_V = []
    T = [T_0]
    for i in range (1, int(duration/resolution)):
        T_V.append(ENERGY_TEMP(T[i-1], Time[i-1], a,b,c,P))
        T.append(T[i-1] + T_V[i]*resolution)
    return Time, T, T_V
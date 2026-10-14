# If speed is v(t) = 2t, the distance from 0 to 5 seconds is the integral of speed over that time

from scipy.integrate import quad
def speed(t):
    return 2*t 
distance,error=quad(speed,0,5)
print(distance)
print(error)
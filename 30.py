from scipy.interpolate import interp1d
time=[1,2,3,4]
temperature=[20,25,31,40]
f=interp1d(time,temperature)
result=f(2.5)
print("temp at 2.5:",float(result))
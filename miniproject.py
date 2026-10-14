from scipy.stats import pearsonr, ttest_ind, linregress
import numpy as np
age=np.array([22,23,24,25,26,30,40])
salary=np.array([20000,3000,4000,25000,30000,40000,50000])
exp=np.array([1,2,3,4,5,6,7])
performance=np.array([2,3,4,5,6,7,8])


# correlation analysis
print("=====correlation analysis:=======")
r,p=pearsonr(exp,salary)
print("salary vs exp:",r,p)
r2,p2=pearsonr(exp,performance)
print("exp vs performance:",r2,p2)
r3,p3=pearsonr(performance,salary)
print("performance vs salary:",r3,p3)


# statasical data
print("======statastics=======:")
low=salary[performance<=5]
high=salary[performance>5]
t,p_value=ttest_ind(low,high)
print("t:",t)
print("p_value:",p_value)


# linear regresion
print("======linear regression=====:")
result=linregress(exp,salary)
print("slope:",result.slope)
print("intercept:",result.intercept)
print("r_sqr:",result.rvalue**2)
print("regression p_value:",p_value)

print("===significant value======:")
for name, value in [
    ("Experience vs Salary", p),
    ("exp vs Performance", p2),
    (" Performance vs salary", p3),
    ("Salary Group Comparison", p_value)
]:
    if value < 0.05:
        print(name, "is significant")
    else:
        print(name, "is not significant")

print("\n=== Conclusion ===")

if r > 0:
    print("Salary tends to increase with experience.")
elif r < 0:
    print("Salary tends to decrease with experience.")
else:
    print("No linear correlation was found.")

if result.pvalue < 0.05:
    print("The regression relationship is statistically significant.")
else:
    print("The regression relationship is not statistically significant.")





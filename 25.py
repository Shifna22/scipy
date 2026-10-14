from scipy.stats import linregress

hours = [1, 2, 3, 4, 5, 6]
marks = [35, 40, 50, 55, 65, 70]
result = linregress(hours, marks)
print("Slope:", result.slope)
print("Intercept:", result.intercept)
print("Correlation:",result.rvalue)
print("P-value:",result.pvalue)
print("Regression equation: Marks =",result.slope,"* Hours +",result.intercept)
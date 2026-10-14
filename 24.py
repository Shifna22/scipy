from scipy.stats import pearsonr

height =[150, 155, 160, 162, 165, 168, 170, 175, 178, 180]
weight =[45, 48, 52, 54, 57, 60, 62, 68, 70, 75]

r,p_value =pearsonr(height, weight)

print("Pearson correlation:", r)
print("P-value:", p_value)

if p_value < 0.05:
    print("Height and weight are significantly correlated")
else:
    print("No significant correlation")
    
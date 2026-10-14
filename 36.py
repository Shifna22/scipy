from scipy.stats import chisquare
observed=[25,30,35,40]
expected=[20,30,40,40]
chi2,p_value=chisquare(f_obs=observed,f_exp=expected)
print("chisquare:",chi2)
print("p_value:",p_value)
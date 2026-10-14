from scipy import stats
exam1=[10,20,30,40,50,60]
exam2=[20,30,40,60,70,80]
t_stat,p_value=stats.ttest_ind(exam1,exam2)
print("tstats:",t_stat)
print("p_value:",p_value)
if p_value< 0.5:
    print("means are different")
else:
    print("means are not diffrent")
from scipy.io import savemat, loadmat
data={"marks:"[55,56,78,56,98]}
savemat("student_data.mat",data)
loaded=loadmat("student_data.mat")
print(loaded["mark"])




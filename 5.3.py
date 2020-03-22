import numpy as np
x0=np.ones(10)
x1=np.array([64.3,99.6,145.45,63.75,135.46,92.85,86.97,144.76,59.3,116.03])
x2=np.array([2,3,4,2,3,4,2,4,1,3])
y=np.array([62.55,82.42,132.62,73.31,131.05,86.57,85.49,127.44,55.25,104.84])
X=np.concatenate((x0,x1,x2),axis=0)
X=X.reshape(3,10)
X1=np.mat(X)
X1=X1.T
X=np.array(X1)
Y=y.reshape(10,1)
X=np.mat(X)
Y=np.mat(Y)
W=(((X.T)*X).I)*(X.T)*Y
print(X)
print(Y)
print(W)
print("W的shape属性结果是:",W.shape)

import math
import tensorflow as tf
import numpy as np
x=np.array([64.3,99.6,145.45,63.75,135.46,92.85,86.97,144.76,59.3,116.03])
y=np.array([62.55,82.42,132.62,73.31,131.05,86.57,85.49,127.44,55.25,104.84])
X=tf.constant(x)
Y=tf.constant(y)
n=np.size(x)
w1=n*(tf.reduce_sum(tf.multiply(X,Y)))
w2=tf.reduce_sum(X)*tf.reduce_sum(Y)
w3=n * tf.reduce_sum(tf.square(X))
w4=math.pow(tf.reduce_sum(X),2)
w=(w1-w2)/(w3-w4)
b=(tf.reduce_sum(Y) - w * (tf.reduce_sum(X)))/n
print("w的值为:",w)
print("b的值为:",b)
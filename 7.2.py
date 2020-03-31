import tensorflow as tf
import matplotlib. pyplot as plt
import numpy as np
mnist = tf.keras.datasets.mnist
(train_x, train_y), (test_x, test_y) = mnist.load_data("D:\Vscode\project1\mnist.npz") 
# (train_x, train_y), (test_x,test_y) = tf.keras.datasets.mnist.load_data()
plt.rcParams['font.sans-serif']=['SimHei']
plt.figure(figsize=(6,6))
plt.suptitle("MNIST测试集样本",color="red",fontsize=20)
for i in range(16):
    num=np.random.randint(1,60000)
    plt.subplot(4,4,i+1)
    plt.axis("off")
    plt.imshow(train_x[num],cmap='gray')
    plt.title("标签值:"+str(train_y[num]),fontsize=14)
plt.tight_layout(rect=[0.1, 0.9, 0, 0.9])
plt.show()

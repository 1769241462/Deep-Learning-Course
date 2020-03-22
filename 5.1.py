import numpy as np

np.random.seed(612)
arr=np.random.rand(1000)
indexNum=int(input("请输入一个1-100之间的整数:"))
print("序号  索引值   随机数")
i=1
index=0
for index in range(arr.size):
    if index % indexNum == 0:
        print(i,index,arr[index])
        i=i+1
import tensorflow as tf
import numpy as np
import tkinter as tk
from tkinter import filedialog
import time
import pandas as pd

import stock_predict as pred


def creat_windows():
    win = tk.Tk()  # 创建窗口
    sw = win.winfo_screenwidth()
    sh = win.winfo_screenheight()
    ww, wh = 800, 450
    x, y = (sw - ww) / 2, (sh - wh) / 2
    win.geometry("%dx%d+%d+%d" % (ww, wh, x, y - 40))  # 居中放置窗口

    win.title('LSTM股票预测')  # 窗口命名

    f_open =open('dataset_2.csv')
    canvas = tk.Label(win)
    canvas.pack()

    var = tk.StringVar()  # 创建变量文字
    var.set('选择数据集')
    tk.Label(win, textvariable=var, bg='#C1FFC1', font=('宋体', 21), width=20, height=2).pack()

    tk.Button(win, text='选择数据集', width=20, height=2, bg='#FF8C00', command=lambda: getdata(var, canvas),
              font=('圆体', 10)).pack()

    canvas = tk.Label(win)
    L1 = tk.Label(win, text="选择你需要的 列(请用空格隔开，从0开始）")
    L1.pack()
    E1 = tk.Entry(win, bd=5)
    E1.pack()
    button1 = tk.Button(win, text="提交", command=lambda: getLable(E1))
    button1.pack()
    canvas.pack()
    win.mainloop()

def getLable(E1):
    string = E1.get()
    print(string)
    gettraindata(string)

def getdata(var, canvas):
    global file_path
    file_path = filedialog.askopenfilename()
    var.set("注，最后一个为label")
    # 读取文件第一行标签
    with open(file_path, 'r', encoding='gb2312') as f:
    # with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()  # 读取所有行
        data2 = lines[0]
    print()

    canvas.configure(text=data2)
    canvas.text = data2

def gettraindata(string):
    f_open = open(file_path)
    df = pd.read_csv(f_open)  # 读入股票数据
    list = string.split()
    print(list)
    x = len(list)
    index=[]
    # data = df.iloc[:, [1,2,3]].values  # 取第3-10列 （2:10从2开始到9）
    for i in range(x):
        q = int(list[i])
        index.append(q)
    global data
    data = df.iloc[:, index].values
    print(data)
    main(data)

def main(data):
    pred.LSTMtest(data)
    var.set("预测的结果是：" + answer)

if __name__ == "__main__":
    creat_windows()

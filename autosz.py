import xlrd
import xlwt
import numpy as np
import pandas as pd
import  math
#分析的城市数 citynum
citynum = 3
data = xlrd.open_workbook('D:/Git/myfreecode/熵值自动化计算/自动熵值法.xls') #读取流量数据
table = data.sheets()[0]                #通过索引顺序获取
h= table.ncols                          #数据表的列数

#通过下面这个方法一次性把数据表读取到矩阵a里
a1=table.col_values(2)                  #读取第1列代码数据
for i in range (3,h):                   #由于上一行有了第一列，这里只需要从第二列开始读取
   a0=table.col_values(i)               #读取第1列代码数据
   a1=np.vstack((a1,a0))                #合并两列，合并后是横着排的，需要转置
a=np.transpose(a1)                      #矩阵转置
line = a[1:]                            #截取下面的数据
line = line.astype(float)
print("处理的数据",line)
print("--"*10)
line.astype(float)
line_max = np.max(line, axis=1)         #每行的最大值
#print(line_max)
line_min = np.min(line, axis=1)         #每行的最小值
#print(line_min)
chazhi = line_max - line_min
line_min1 = np.tile(line_min,(3,1)).T   #最小值扩展到5*3的数列
chazhi1 = np.tile(chazhi,(3,1)).T       #差值的扩展
temp = (line - line_min1)/chazhi1       #无量纲化处理后的数据
temp = temp + 0.0001                    #处理偏差
tempsum = np.sum(temp, axis=1)          #每行求和
tempsum = np.tile(tempsum,(3,1)).T
p = temp / tempsum                      #求p值
plnp = p * np.log(p)
plnpsum = np.sum(plnp, axis=1)
#计算熵值
shangzhi = (-1/math.log(citynum))*plnpsum
#计算差异系数
e = (1 - shangzhi)
esum = np.sum(e, axis=0)                #差异值求和
#计算权重
qz = e / esum
print("对应参数权重",qz)
qz1 = np.tile(qz,(3,1)).T
score = qz1 * p
scoresum = np.sum(score, axis=0)          #每列求和
print("各城市权重得分",scoresum)


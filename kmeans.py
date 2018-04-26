# coding=utf-8
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from mpl_toolkits.mplot3d import Axes3D
X = []
Y =[]
f = open('testSet.txt',encoding='utf-8', errors='ignore')
g = open('testSet.txt',encoding='utf-8', errors='ignore')
for v in g:

    Y.append([v.split(',')[0],float(v.split(',')[1]), float(v.split(',')[2]), float(v.split(',')[3])])
print(Y)
for v in f:
    X.append([float(v.split(',')[1]), float(v.split(',')[2]), float(v.split(',')[3])])
# 转换成numpy array
X = np.array(X)
print(X)
# 类簇的数量
n_clusters = 3
# 现在把数据和对应的分类书放入聚类函数中进行聚类
cls = KMeans(n_clusters).fit(X)
print(cls)
# X中每项所属分类的一个列表
cls.labels_
# 画图
pca = PCA(n_components=3)
markers = ['^', 'x', 'o', '*', '+']
fig=plt.figure()
ax=fig.add_subplot(111,projection='3d')
print(cls.labels_)
for i in range(n_clusters):
    members = cls.labels_ == i
    print(members)
    ax.scatter(X[members, 0], X[members, 1],X[members,2], s=60, marker=markers[i], c='b', alpha=0.5)


myfont = matplotlib.font_manager.FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=14)
for j in Y:
    print(j[0])
    ax.text(j[1],j[2],j[3],j[0],fontproperties=myfont)
plt.title('')
plt.show()  
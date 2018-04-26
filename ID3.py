from sklearn.datasets import load_breast_cancer
from id3 import Id3Estimator
from id3 import export_graphviz

X = [['销售部','高级','31-40'],
     ['销售部','初级','21-30'],
     ['销售部',"初级",'31-40'],
     ['系统部','初级','21-30'],
     ['系统部','高级','31-40'],
     ['系统部','初级','21-30'],
     ['系统部','高级','41-50'],
     ['市场部','高级','31-40'],
     ['市场部','初级','31-40'],
     ['秘书处','高级','41-50'],
     ['秘书处','初级','21-30']]
Y =['C2','C3','C3','C2','C1','C2','C1','C2','C2','C3','C3']
f = ['部门','级别','年龄']
estimator = Id3Estimator()
estimator.fit(X, Y,check_input=True)
export_graphviz(estimator.tree_, 'tree.dot', f)
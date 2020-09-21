import xlrd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer  
from sklearn.feature_extraction.text import TfidfVectorizer


#打开文件  
table = xlrd.open_workbook('dataSet.xlsx').sheets()[0]  
dataSet = table.col_values(0)

#训练标签集
data = [['' for col in range(5)] for row in range(200)]
for i in range(200):
	temp = table.row_values(i)
	for j in range(2,7):
		if temp[j] is not '':
			data[i][j-2] = temp[j]

condition = lambda t: t != "" 

for i in range(200):
	data[i] = list(filter(condition, data[i]))
# 构造权值字典
weightlist = {}
b = str(data)
b = b.replace('[','')
b = b.replace(']','')
a = list(eval(b))
for i in set(a):
	weightlist[i] = 1/a.count(i)
# 
# 
#测试标签集
dataTest = [['' for col in range(5)] for row in range(30)]
for i in range(30):
	temp = table.row_values(200+i)
	for j in range(2,7):
		if temp[j] is not '':
			dataTest[i][j-2] = temp[j]
for i in range(30):
	dataTest[i] = list(filter(condition, dataTest[i]))

resultlist = [[0 for col in range(200)] for row in range(30)]
resultIndex = [[0 for col in range(200)] for row in range(30)]

#权值列表
for i in range(len(dataTest)):
	testTag = dataTest[i]
	for j in range(len(testTag)):
		for k in range(200):
			if(testTag[j] in data[k]):
				resultlist[i][k] += weightlist[testTag[j]]
				resultIndex[i][k] = k
				if(k==0):
					resultIndex[i][k] = 999

#最佳推荐列表
toplist = []
topName = [['' for col in range(5)] for row in range(30)]

def topN(n,x=[]):
    a = x[:]
    Tindex = []
    while n>0:
        Tindex.append(a.index(max(a)))
        a[a.index(max(a))] = -999
        n = n-1
    return Tindex
for i in range(30):
	toplist.append(topN(5,resultlist[i]))
for i in range(len(toplist)):
	for j in range(len(toplist[j])):
		topName[i][j] = dataSet[toplist[i][j]]

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation
import numpy as np
import xlrd  
import xlwt  
from xlutils.copy import copy  

import tag

data = xlrd.open_workbook('Segmentation.xls').sheets()[0].col_values(2)
stpwrdpath = "stop_words.txt"
stpwrd_dic = open(stpwrdpath, 'rb')
stpwrd_content = stpwrd_dic.read()
#将停用词表转换为list  
stpwrdlst = stpwrd_content.splitlines()
stpwrd_dic.close()
wb = xlwt.Workbook(encoding='utf-8')#创建excel文件，声明编码
# 
resultIndex = tag.resultIndex
cntVector = CountVectorizer(stop_words=stpwrdlst)
for i in range(len(resultIndex)):
	item = []
	temp = list(filter(lambda t: t != 0, resultIndex[i]))#相关文本下标  用于主题模型训练
	for n in range(len(temp)):
		if temp[n] == 999:
			temp[n]=0
		item.append(data[temp[n]]) 
	item.append(data[199+i])
	print(len(item))
	cntTf = cntVector.fit_transform(item)
	lda = LatentDirichletAllocation(n_topics=6,
	                                learning_offset=50.,
	                                random_state=0)
	docres = lda.fit_transform(cntTf)
	doclist = docres.tolist()
	sheet = "Sheet" + str(i+1)
	print(sheet)
	ws = wb.add_sheet(sheet,cell_overwrite_ok=True)#创建表格
	for j in range(len(docres)):
		for k in range(len(docres[j])):
			ws.write(j,k,doclist[j][k])	

wb.save('LDA_6_2.xls')  

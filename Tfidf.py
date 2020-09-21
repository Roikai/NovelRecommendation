# coding:utf-8  
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer  
from sklearn.feature_extraction.text import TfidfTransformer 
from sklearn.feature_extraction.text import HashingVectorizer 
from sklearn.feature_extraction.text import TfidfVectorizer
import xlwt

# with open('./nlp_test1.txt') as f3:
#     res1 = f3.read()
# with open('./nlp_test3.txt') as f4:
#     res2 = f4.read()
# with open('./nlp_test5.txt') as f5:
#     res3 = f5.read()

# stpwrdpath = "stop_words.txt"
# stpwrd_dic = open(stpwrdpath, 'rb')
# stpwrd_content = stpwrd_dic.read()

# stpwrdlst = stpwrd_content.splitlines()
# stpwrd_dic.close()

# corpus =  [res1,res2,res3]

# CountVectorizer  tf-idf
# vectorizer = CountVectorizer(stop_words=stpwrdlst)
# cnt = vectorizer.fit_transform(corpus)
# print("CountVectorizer:\n")
# #类调用  
# transformer = TfidfTransformer()  
# # print(transformer)  
# #将词频矩阵X统计成TF-IDF值  
# tfidf = transformer.fit_transform(cnt)  
# #查看数据结构 tfidf[i][j]表示i类文本中的tf-idf权重  
# print(tfidf.toarray())



# TfidfVectorizer   tf-idf 
# tfidf = TfidfVectorizer(stop_words=stpwrdlst)
# cntTf = tfidf.fit_transform(corpus)
# print("tfidf:\n")
# print(cntTf)
# 
# 
#hash  向量是被归一化到-1到1之间
# vectorizer = HashingVectorizer(stop_words =stpwrdlst) 
# cntTf = vectorizer.fit_transform(corpus)
# print("vectorizer:\n")
# print(cntTf) 




# 统计每个词语的tf-idf权值
# vectorizer = CountVectorizer(stop_words=stpwrdlst)
# transformer = TfidfTransformer()
# #第一个fit_transform是计算tf-idf，第二个fit_transform是将文本转为词频矩阵
# tfidf = transformer.fit_transform(vectorizer.fit_transform(corpus))  
# wordlist = vectorizer.get_feature_names()#获取词袋模型中的所有词  
# weightlist = tfidf.toarray()  

# newTable="mutclass.xls"#表格名称
# wb = xlwt.Workbook(encoding='utf-8')#创建excel文件，声明编码
# ws = wb.add_sheet('sheet1',cell_overwrite_ok=True)#创建表格

# headData = []#表头部信息
# for j in range(len(wordlist)): 
# 	headData.append(wordlist[j])
# for colnum in range(0, len(wordlist)):
# 	ws.write(0, colnum, headData[colnum], xlwt.easyxf('font: bold on'))  # 行，列

# for i in range(len(weightlist)):  
#     # print("-------这里输出第",i,"类文本的词语tf-idf权重------"  )
#     # print(weightlist[i][np.argpartition(weightlist[i],-3)[-3:]])	
#     for j in range(len(wordlist)): 
#   	 	ws.write(i+1,j,weightlist[i][j])
# wb.save(newTable)

import xlrd


file = xlrd.open_workbook('dataSet.xlsx')  
table = file.sheets()[0]
tag = []
for i in range(3,7):
	data = table.col_values(i)
	tag.append(data)
array = np.array(tag).reshape(-1)  


# checked = []
# for i in range(len(array)):
# 	if array[i] not in checked:
# 		checked.append(array[i])
# print(checked)
# print(len(checked))

vectorizer = CountVectorizer()
cnt = vectorizer.fit_transform(array)
wordlist = vectorizer.get_feature_names()

print(array)



# TfidfVectorizer   tf-idf 
tfidf = TfidfVectorizer()
cntTf = tfidf.fit_transform(array)
print(cntTf)


  # (0, 73)	1.0
  # (1, 512)	1.0
  # (2, 43)	0.6884293917020166
  # (2, 221)	0.7253033659378615
  # (3, 780)	1.0
  # (4, 736)	1.0
  # (5, 753)	0.7071067811865476
  # (5, 88)	0.7071067811865476
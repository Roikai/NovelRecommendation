import xlrd  
import numpy as np
import tag
import xlwt  

file = xlrd.open_workbook('LDA_6_2.xls')  
dataSet = xlrd.open_workbook('dataSet.xlsx').sheets()[0].col_values(0)
content = xlrd.open_workbook('dataSet.xlsx').sheets()[0].col_values(1)

#计算余弦相似度函数
def cos_like(x,y): 
    tx = np.array(x)
    ty = np.array(y)
    cos1 = np.sum(tx*ty)
    cos21 = np.sqrt(sum(tx**2))
    cos22 = np.sqrt(sum(ty**2))
    return cos1/float(cos21*cos22)

#最大的N个数的下标
def topN(n,x=[]):
    a = x[:]
    Tindex = []
    while n>0:
        Tindex.append(a.index(max(a)))
        a[a.index(max(a))] = -999
        n = n-1
    return Tindex


wb = xlwt.Workbook(encoding='utf-8')#创建excel文件，声明编码
ws = wb.add_sheet("sheet1",cell_overwrite_ok=True)#创建表格
#计算相似的主题向量
for i in range(30):
    data = []
    index = []
    result = []
    itemName = []
    table = file.sheets()[i]#与第i个文本相关的文本向量标签
    test = table.row_values(table.nrows-1) #测试数据

    for j in range(table.nrows-1):
        sim = cos_like(test,table.row_values(j))
        data.append(sim) 
        index = topN(5,data)
    temp = list(filter(lambda t: t != 0, tag.resultIndex[i]))
    for n in range(len(temp)):
        if temp[n] == 999:
            temp[n]=0
    for k in range(len(index)):
        itemName.append(dataSet[temp[index[k]]])
        result.append(temp[index[k]]) 
    # print(result)

    target = "《"+dataSet[200+i]+"》"+":"+content[200+i]
    if(i<1):
        ws.write(i,0,target) 
    else:
        ws.write(3*i,0,target) 
    ws.write(3*i+1,0,"纯标签推荐")
    ws.write(3*i+2,0,"主题模型推荐")
    for q in range(len(tag.toplist[i])):
        ws.write(3*i+1,q+1,"《"+dataSet[tag.toplist[i][q]]+"》"+":"+content[tag.toplist[i][q]])
    for r in range(len(result)):
        ws.write(3*i+2,r+1,"《"+dataSet[result[r]]+"》"+":"+content[result[r]])


wb.save('result.xls')
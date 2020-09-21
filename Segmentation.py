import jieba
import xlrd
import xlwt

#打开文件  
file = xlrd.open_workbook('dataSet.xlsx')  
#打开工作表  
table = file.sheets()[0]  

data = table.col_values(1)
cutAccurate = []
cutAll = []
cutSearch = []

newTable="Segmentation.xls"#表格名称 
wb = xlwt.Workbook(encoding='utf-8')#创建excel文件，声明编码
ws = wb.add_sheet('sheet1',cell_overwrite_ok=True)#创建表格
headData = ['精确模式','全模式','搜索引擎模式']#表头部信息
for colnum in range(len(headData)):
    ws.write(0, colnum, headData[colnum], xlwt.easyxf('font: bold on'))  # 行，列


for i in range(len(data)):
    document1 = jieba.cut(data[i])#精确模式
    result1 = ' '.join(document1)
    cutAccurate.append(result1)
    document2 = jieba.cut(data[i],cut_all=True) #全模式
    result2 = ' '.join(document2)
    cutAll.append(result2)
    document3 = jieba.cut_for_search(data[i])    #搜索引擎模式
    result3 = ' '.join(document3)
    cutSearch.append(result3)

for i in range(len(cutAccurate)):
    ws.write(i+1,0,cutAccurate[i])
    ws.write(i+1,1,cutAll[i])
    ws.write(i+1,2,cutSearch[i])
wb.save(newTable)


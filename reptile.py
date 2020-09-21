# -*- coding: utf-8 -*-
# 
import requests
import re
from bs4 import BeautifulSoup
import xlwt
import bs4

headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'} 

formData={  
    "redir":"https://book.douban.com/tag/",  
    "form_email":"718524381@qq.com",  
    "form_password":"hanze6313",  
    "login":"登录"
}  


def getHtmlText(url):
	try:
		r = requests.get(url,data=formData,headers=headers)
		r.raise_for_status()
		return r.text
	except:
		return ""

def fillUnivList(ulist,html):
	soup = BeautifulSoup(html,"html.parser")
	tb = soup.find('div',{'class':'article'}).find_all('table',{'class': 'tagCol'})
	for tr in tb:
		if isinstance(tr,bs4.element.Tag):
			tds = tr('td')
			for i in range(len(tds)):
				ulist.append(tds[i].a.string)

def fillUnivList2(ulist,html):
	soup = BeautifulSoup(html,"html.parser")
	tb = soup.find_all('a',{'class':'nbg'})
	for i in range(len(tb)):
		ulist.append(tb[i]['href']) 		

def excel_write(row,ulist,ws):
	for i in range(0,len(ulist)):
		ws.write(row,i,ulist[i])#行，列，数据
	
def fillUnivList3(ulist,html):
	soup = BeautifulSoup(html,"html.parser")
	bd = soup.find('div',{'class':'article'})
	title = bd.find('a',{'class':'nbg'})['title']
	pTag = bd.find('div',{'class':'intro'}).find_all('p')
	ptext = ''	
	for i in range(len(pTag)):
		ptext += pTag[i].string
	ulist.append(title)#标题
	ulist.append(ptext)#摘要
	tag = ['']*5
	MulTag = bd.find('div',{'id':'db-tags-section'}).find('div',{'class':'indent'}).find_all('a')#标签列表
	for i in range(5):
		ulist.append(MulTag[i].string)

def getTag():
	tag = []
	url = 'https://book.douban.com/tag/'
	html = getHtmlText(url)
	fillUnivList(tag,html)
	return tag

def getItemUrl(tag):
	itemUrl = []
	for i in range(len(tag)):
		print(tag[i])
		url = 'https://book.douban.com/tag/'+ str(tag[i])
		html = getHtmlText(url)
		fillUnivList2(itemUrl,html)
	return itemUrl

def main():
	newTable="dataSet.xls"#表格名称	
	wb = xlwt.Workbook(encoding='utf-8')#创建excel文件，声明编码
	ws = wb.add_sheet('sheet1',cell_overwrite_ok=True)#创建表格
	headData = ['书名','摘要','标签1','标签2','标签3','标签4','标签5',]#表头部信息
	for colnum in range(len(headData)):
		ws.write(0, colnum, headData[colnum], xlwt.easyxf('font: bold on'))  # 行，列
	row = 1
	for i in range(len(urlList)):
		try:
			url = urlList[i]
			uinfo = []
			html = getHtmlText(url)
			fillUnivList3(uinfo,html)
			row = row+1
			excel_write(row,uinfo,ws)
			wb.save(newTable)
		except:
			print("第"+str(i)+"个url出错")
		
if __name__ == '__main__':
	main()

import xlrd
from core.my_request import  MyRequest
from conf.seting import CASE_PATH
import os
#获取excel的函数

path=os.path.join(CASE_PATH,'测试用例.xls')

#path.replace()
print(path)

def get_case(path):
    book=xlrd.open_workbook(path) #最好加个r
    sheet=book.sheet_by_index(0)
    all_case=[]
    for i in range(1,sheet.nrows):
        all_case.append(sheet.row_values(i,4,8))
    return all_case
#发送请求
def send_request(url,method,data,headers=None):
    test=MyRequest(url,data,headers=headers)
    if method.upper()=='POST':
        res=test.post()
    elif method.upper()=='GET':
        res=test.get()
    else:
        res={'data':'暂不支持该请求类型'}
    return res['data']

import xlrd
from xlutils.copy import copy
import os
import datetime
from conf import seting
import yagmail
def make_today_dir():
    #创建当天的文件夹，返回绝对路径
    today = str(datetime.date.today())
    #c:/xxx/xxx/atp/report/2018-11-24/测试用例.xls
    abs_path = os.path.join(seting.REPORT_PATH,today)
    #拼成当天的绝对路径
    if os.path.exists(abs_path):
        pass
    else:
        os.mkdir(abs_path)

    return abs_path

def write_res(case_path,case_res):
    #c:/xxx/xxx/atp/cases/测试用例.xls
    #[ ['{"xdfsdf}','通过'],['{"xdfsdf}','失败'] ]
    book = xlrd.open_workbook(case_path)
    new_book = copy(book)
    sheet = new_book.get_sheet(0)
    for row,res in enumerate(case_res,1):
        response,status = res
        sheet.write(row,8,response)
        sheet.write(row,9,status)
        #写第8列和第9列
    cur_date_dir = make_today_dir()#创建当前文件夹，并且返回绝对路径
    file_name = os.path.split(case_path)[-1] #只获取到filename
    cur_time = datetime.datetime.today().strftime('%H%M%S') #获取到当天时分秒
    new_file_name = cur_time+'_'+file_name #165530_测试用例.xls
    real_path = os.path.join(cur_date_dir,new_file_name)#拼路径
    new_book.save(real_path)
    return real_path

def send_mail(content,file_path=None):
    #发邮件，传入邮件正文和附件
    m = yagmail.SMTP(**seting.MAIL_INFO,)
    subject = '接口测试报告_%s'%str(datetime.datetime.today())
    m.send(subject=subject,to=seting.TO,contents=content,attachments=file_path)
import os
#os.path.abspath(__file__)文件所在路径
#os.path.dirname文件所在目录
BASE_PATH=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOG_PATH=os.path.join(BASE_PATH,'logs')#拼接路径
CASE_PATH=os.path.join(BASE_PATH,'cases')
REPORT_PATH=os.path.join(BASE_PATH,'report')

#邮箱发送所需的一些信息
MAIL_INFO={
        'user':'hongweili163@163.com',
        'password':'QFCLVOOJFGHOUWAV',
         'host':'smtp.163.com'
}
TO=['158964462@qq.com','1632020181@qq.com']



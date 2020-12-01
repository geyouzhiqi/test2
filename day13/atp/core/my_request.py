import requests
import nnlog
import os
from conf.seting import LOG_PATH
import jsonpath
class MyRequest:
    log_file_name=os.path.join(LOG_PATH,'mytest.log')
    timeout=10 #类属性
    #如果初始化函数里面写了一些参数，实例化时就要加上这些参数，如果没写在方法中写了，只需要在调用方法时写上参数即可
    #后面方法如果想调用实例化参数，需要加上self.
    def __init__(self, url, data=None, headers=None, file=None):
        self.url = url
        self.data = data
        self.headers = headers
        self.file = file
#get请求
    def get(self):
        try:
            req=requests.get(url=self.url,params=self.data,headers=self.headers,files=self.file,timeout=self.timeout)
        except Exception as e:
            res={'staus':'0','data':e}
        else:
            try:
                res = {'staus': '1', 'data': req.json()} #json是方法，text是属性，如果返回的不是json就把整个页面爬下来
                #print(res['data'])
            except Exception as e:
                res={'staus': '2', 'data': req.text}
        log_str='url： %s 请求方式：post  data：%s ,返回数据：%s'%(self.url,self.data,res)
        self.write_log(log_str)
        return(res)
        #post请求
    def post(self):
        try:
            req=requests.post(url=self.url,data=self.data,headers=self.headers,files=self.file,timeout=self.timeout)
        except Exception as e:
            res={'staus':'0','data':e}
        else:
            try:
                res = {'staus': '1', 'data': req.json()} #json是方法，text是属性，如果返回的不是json就把整个页面爬下来
               # print(res)
            except Exception as e:
                res={'staus': '2', 'data': req.text}
        log_str='url： %s 请求方式：post  data：%s ,返回数据：%s'%(self.url,self.data,res)
        self.write_log(log_str)
        return(res)
    @classmethod
        #类方法使用类变量时需要用cls
    def write_log(cls,content):
            log = nnlog.Logger(cls.log_file_name)
            log.debug(content)

if __name__ == '__main__':
    url = 'http://api.nnzhp.cn/api/user/login'
    data = {'username': 'niuhanyang', 'passwd': 'aA123456'}
    # data = {'stu_name':'niuhanyang'}
    p=MyRequest(url,data)
    res=(p.post())
    print(res['data']['error_code'])
    # key='error_code'
    # res = jsonpath.jsonpath(p.post(), '$..%s' %key)

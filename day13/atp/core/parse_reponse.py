import  jsonpath
from core.my_request import MyRequest
from core.parse_param import ParseParam
# jsonpath是用在json数据里面的分层结构取值用的
class ResponseParse:
    seqs = ['!=', '>=', '<=', '=', '<', '>', 'in', 'notin']
    def __init__(self,response,check):
        self.response=response
        self.check=check

    # error_code=0,userId=1需要将其分成，’error_code‘ ’= ’’0‘

    def format_check(self):
        tmp_list=[]
        check_list=[]
        check_list=self.check.split(',')
        print(check_list)
        for seq in check_list:
            for s in self.seqs:
                if s in seq:
                    if len(seq.split(s))>1:
                        k,v=seq.split(s)
                        tmp=[k,s,v]
                        tmp_list.append(tmp)
                        break
        return tmp_list

    def get_real_value(self,key):
        #试一下结果
        res=jsonpath.jsonpath(self.response,'$..%s'%key)#进入两层目录
        if res:
            return res[0]
        else:
            return '找不到该key【%s】' % key

    #运算符检查结果对比，根据测试用例的期望内容与返回的实际内容进行校验
    def operation_check(self,real,seq,hope):
        msg = "判断信息：%s %s %s " % (real, seq, hope)
        real = str(real)  # 为了保持类型一致
        if seq=='=':
            status=real==hope
        elif seq=='!=':
            status=real!=hope
        elif seq=='in':
            status=real in hope
        elif seq=='notin':
            status=real not in hope
        else:
            status, msg = self.num_check(real, seq, hope)
        return status,msg

    def num_check(self,real,seq,hope):
        msg = "判断信息：%s %s %s " % (real, seq, hope)
        try:
            real=float(real)
            hope=float(hope)
        except Exception as e:
            msg='判断是数字类型出错%s %s %s ' % (real, seq, hope)
            status=False
        else:
            if seq=='>':
                status=real>hope
            elif seq=='<':
                status=real<hope
            elif seq=='<=':
                status=real<=hope
            else:
                status=real>=hope
            return status,msg
    #整个检查过程
    def check_res(self):
        check_list=self.format_check()
        all_msg=''
        for check in check_list:#循环所有的检查点
            key,seq,hope = check
            real = self.get_real_value(key)
            status,msg = self.operation_check(real,seq,hope)
            all_msg = all_msg+msg+'\n' #累加提示信息
            if status:
                pass
            else:
                return '失败',all_msg
        return '通过',all_msg

if __name__ == '__main__':
    url = 'http://api.nnzhp.cn/api/user/login'
    param = 'username=niuhanyang' \
            ',phone=<phone>,email=<email>' \
            ',id_card=<id_card>,start_time=' \
            '<cur_time>,balan=<money>'
    pdata = ParseParam(param)
    data = pdata.strToDict()
    print(data)
    p = MyRequest(url, data)
    res = (p.post())
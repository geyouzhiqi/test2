import os,sys
BAE_PATH  = os.path.dirname(
os.path.dirname(os.path.abspath(__file__))
) #atp的目录
sys.path.insert(0,BAE_PATH)

from conf.seting import CASE_PATH
from core import case_operation,parse_param,parse_reponse
from core import tools
import glob
class RunCase:
    content = '''
    各位好！
        本次测试结果：总共运行%s条用例，通过%s条，失败%s条。详细信息见附件。
    '''
    def get_excel(self):
        #s='/Users/nhy/test*.xls'
        for excel in glob.glob(os.path.join(CASE_PATH,'测试用例*.xls')):
            cases = case_operation.get_case(excel)#调用读取excel的函数
            results = self.send_requests(cases) #发送请求，并校验结果
            report_file_path = tools.write_res(excel,results)#写入结果
            all_count = len(cases) #总共多条用例
            fail_count = all_count - self.success_count
            content = self.content%(all_count,self.success_count,fail_count)
            tools.send_mail(content,report_file_path)
    def send_requests(self,cases):
        #    #[[url,get,data,check],[url,get,data,check]]
        self.success_count = 0
        results = []
        for case in cases:
            url,method,param,check = case #获取到每条用例的参数
            p = parse_param.ParseParam(param) #解析请求参数
            data = p.strToDict()#请求参数转成字典
            response = case_operation.send_request(url,method,data)#发请求
            #下面这2行代码是判断用例执行是否通过的
            p2 = parse_reponse.ResponseParse(response,check)
            status, msg = p2.check_res()#调用写好的校验结果方法,
            real_res = str(response)+'\n'+msg #是把校验的信息和返回的json拼到一起
            results.append([real_res,status]) #这里面的小list是每一个用例运行的结果
            if status == '通过':
                self.success_count += 1 #统计成功的次数
        return results #返回运行的结果

    def main(self):
        print('开始测试'.center(50,'*'))
        self.get_excel()
        print('测试结束'.center(50,'*'))

if __name__ == '__main__':
    run = RunCase()
    run.main()
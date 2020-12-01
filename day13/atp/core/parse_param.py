import random
import string
import  time
'''
这个类的作用就是随机生成一些data数据
'''
class ParseParam:

    func_map=['phone','email','id_card','cur_time']
    def __init__(self,param):
        self.param=param
        self.parse()

    def phone(self):
        phone_start=['134','181','138','177','150','132','188','186','189','130','170','153','155']
        start=random.choice(phone_start)#从phonestart中随机选一个元素
        end=str(random.randint(0,99999999))
        res=start+end.zfill(8)
        return res

    def email(self):
        email_end = ['163.com', 'qq.com', '126.com', 'sina.com']
        end=random.choice(email_end)
        email_start=''.join(random.sample(string.ascii_letters+string.digits,6))#截取制定长度的随机数
        res=email_start+'@'+end
        return res

    def id_card(self):
         id_num='412723'+'19'+''.join(random.sample(string.digits,10))
         return id_num

    def cur_time(self):
        return time.time()

    #利用getattr获取对象里面的属性和方法
    def parse(self):
        for func in self.func_map: #方法要想调用里面的属性必须加上self
            temp=str(getattr(self,func)())
            self.param=self.param.replace('<%s>'%func,temp) #这个地方忘了加上func，替换都不知道替换的啥

    #将字符串转换成字典,最主要的是要确定输入输出数据的类型
    def strToDict(self):
        data={}
        paratmp=self.param.split(',')
        print(paratmp)
        for temp in paratmp:
            p=temp.split('=')
            print(p)
            if len(p)>1:
                k,v=p
                data[k]=p
        return data

        #param = 'username=niuhanyang' \
        #         ',phone=<phone>,email=<email>' \
        #         ',id_card=<id_card>,start_time=' \
        #         '<cur_time>,balan=<money>'






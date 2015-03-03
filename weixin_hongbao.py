# -*- coding:utf-8 -*-
import random
import math
__author__ = 'kiven'

'''
方案1、先根据金额和红包数随机生成每个红包的一个列表，领红包的时候从列表中取
方案2、每个红包最少金额0.01元，最大金额=总金额-(红包数-1)*0.01
'''
# 微信红包算法1
def _weixin_hongbao(money,n):
    # 方案一
    _res = [float('%.2f'%(random.uniform(0.01,money))) for x in xrange(n)]
    _sum = sum(_res) # 求和
    return [float('%.2f'%(x*money/_sum)) for x in _res]

# 微信红包算法2
def _weixin_hongbao_(money,n):
    pass


'''
# 小伙伴排队领
persons = ['aaaa','lee','sb','jack']
hongbao = _weixin_hongbao(10,len(persons))
result = {} # 领取结果
for x in xrange(len(persons)):
    result[persons[x]] = hongbao[x]
print result # 输出结果:{'aaaa': '1.61', 'sb': '2.49', 'lee': '3.02', 'jack': '2.87'}
'''



class Weixin_Hongbao(object):

    # 转换成分
    def __init__(self,money,count):
        self.money = money*100
        self.count = count
        self.max = self.money
        self.min = 1
        self.offset = 1

    # 生成红包
    def generate(self):
        self.result = []
        self.average = self.money / self.count
        for i in range(self.count):
            if self._next(self.max,self.min) > self.average:
                self._money = self.min + math.sqrt(random.randint(self.min,(self.average - self.min)**2))
            else:
                self._money = self.max - math.sqrt(random.randint(self.min,(self.max - self.average)**2))
            self._money = round(self._money)
            self.result.append(self._money)
            self.money -= self._money
        # 自我修补
        self.repair(self.money,self.count,self.max,self.min)
        # 转换成元
        return [x/100 for x in self.result]

    '''
    修补程序
    '''
    def repair(self,total,count,max,min):
        while total > 0:
            for i in range(count):
                if total > 0 and self.result[i] < max:
                    self.result[i] += self.offset;
                    total -= 1
        while total < 0:
            for i in range(count):
                if total < 0 and self.result[i] > min:
                    self.result[i] -= self.offset;
                    total += 1

    def _next(self,max,min):
        return random.randint(min,max - min)



wxhb = Weixin_Hongbao(100,10)
print wxhb.generate()


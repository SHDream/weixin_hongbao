# -*- coding:utf-8 -*-
import random
__author__ = 'kiven'

'''
方案1、先根据金额和红包数随机生成每个红包的一个列表，领红包的时候从列表中取
方案2、每个红包最少金额0.01元，最大金额=总金额-(红包数-1)*0.01
'''
# 微信红包算法1
def _weixin_hongbao(money,n):
    # 方案一
    _res = ['%.2f'%(random.uniform(0,money)) for x in xrange(n)]
    _rev = [float(x) for x in _res] # 换成浮点数字
    _sum = sum(_rev) # 求和
    return ['%.2f'%(x*money/_sum) for x in _rev]

def _weixin_hongbao_(money,n):
    # 方案二
    pass


# 小伙伴排队领
persons = ['aaaa','lee','sb','jack']
hongbao = _weixin_hongbao(10,len(persons))
result = {} # 领取结果
for x in xrange(len(persons)):
    result[persons[x]] = hongbao[x]
print result # 输出结果:{'aaaa': '1.61', 'sb': '2.49', 'lee': '3.02', 'jack': '2.87'}
